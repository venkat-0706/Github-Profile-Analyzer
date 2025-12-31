from fastapi import APIRouter, Request, Form, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.services.github_api import fetch_user_data
from app.services.score_engine import calculate_score
from app.ai.profile_analyzer import (
    generate_ai_feedback,
    get_cached_feedback,
    identify_drawbacks,
    improvement_actions
)
from app.ai.fast_recruiter_rules import fast_recruiter_suggestions

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# ------------------------------
# HOME PAGE
# ------------------------------
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# ------------------------------
# SCORE ANALYSIS
# ------------------------------
@router.post("/score")
async def score(
    request: Request,
    background_tasks: BackgroundTasks,
    username: str = Form(...)
):
    # Fetch GitHub data
    data = fetch_user_data(username)

    # Calculate score
    score, metrics, diagnostics = calculate_score(data)

    # Immediate analysis (fast)
    drawbacks = identify_drawbacks(data)
    improvements = improvement_actions(drawbacks)
    fast_tips = fast_recruiter_suggestions(drawbacks)

    # Background AI refinement
    background_tasks.add_task(
        generate_ai_feedback, username, data, score
    )

    ai_data = get_cached_feedback(username) or {}

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "username": username,
            "score": score,
            "metrics": metrics,
            "diagnostics": diagnostics,
            "drawbacks": drawbacks,
            "improvements": improvements,
            "recruiter_feedback": ai_data.get(
                "recruiter_feedback",
                "\n".join(fast_tips)
            )
        }
    )
