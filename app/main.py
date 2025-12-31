from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
import requests

app = FastAPI()

# ✅ MOUNT STATIC FILES (THIS WAS MISSING)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)

# 🔥 Warm up LLM (optional but recommended)
@app.on_event("startup")
def warmup_llm():
    try:
        requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:2b", "prompt": "Hello"},
            timeout=5
        )
    except:
        pass
