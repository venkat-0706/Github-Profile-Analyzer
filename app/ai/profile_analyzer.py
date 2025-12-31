from app.ai.local_llm_client import call_llm
from app.ai.prompt_templates import build_recruiter_prompt
from app.ai.fast_recruiter_rules import fast_recruiter_suggestions

AI_CACHE = {}

# ---------------------------------
# 1️⃣ Identify current drawbacks
# ---------------------------------
def identify_drawbacks(data: dict) -> list:
    drawbacks = []

    if data["followers"] < 50:
        drawbacks.append(f"Low follower count ({data['followers']})")

    if data["repos"] < 5:
        drawbacks.append(f"Only {data['repos']} public repositories")

    if data["repos"] > 0 and data["repo_descriptions"] / data["repos"] < 0.8:
        drawbacks.append(
            f"Only {data['repo_descriptions']} of {data['repos']} repositories have proper descriptions"
        )

    if (data["stars"] + data["forks"]) < 25:
        drawbacks.append(
            f"Low community engagement (stars + forks = {data['stars'] + data['forks']})"
        )

    if not data["bio"]:
        drawbacks.append("Missing GitHub bio")

    if not data["blog"]:
        drawbacks.append("No portfolio or external website linked")

    return drawbacks


# ---------------------------------
# 2️⃣ Improvements (deterministic)
# ---------------------------------
def improvement_actions(drawbacks: list) -> list:
    improvements = []

    for d in drawbacks:
        if "follower" in d:
            improvements.append(
                "Increase visibility by contributing to popular open-source projects and engaging with the community"
            )
        elif "repositories" in d:
            improvements.append(
                "Add 2–3 meaningful projects that demonstrate real-world problem solving"
            )
        elif "descriptions" in d:
            improvements.append(
                "Write clear repository descriptions explaining purpose, tech stack, and outcome"
            )
        elif "engagement" in d:
            improvements.append(
                "Focus on building impactful projects and promote them within developer communities"
            )
        elif "bio" in d:
            improvements.append(
                "Add a concise GitHub bio highlighting your role, skills, and interests"
            )
        elif "portfolio" in d:
            improvements.append(
                "Link a personal portfolio, LinkedIn, or project website"
            )

    return improvements


# ---------------------------------
# 3️⃣ AI recruiter refinement (optional)
# ---------------------------------
def generate_ai_feedback(username: str, data: dict, score: int):
    drawbacks = identify_drawbacks(data)
    improvements = improvement_actions(drawbacks)

    # 🚀 FAST recruiter tips (always available)
    fast_tips = fast_recruiter_suggestions(drawbacks)

    try:
        prompt = build_recruiter_prompt(drawbacks, improvements, score)
        ai_text = call_llm(prompt)
    except Exception:
        ai_text = None

    # ✅ Always cache something useful
    AI_CACHE[username] = {
        "drawbacks": drawbacks,
        "improvements": improvements,
        "recruiter_feedback": ai_text or "\n".join(fast_tips),
        "source": "ai" if ai_text else "rules"
    }


def get_cached_feedback(username: str) -> dict:
    return AI_CACHE.get(username)
