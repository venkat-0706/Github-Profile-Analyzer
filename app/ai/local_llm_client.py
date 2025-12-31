import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma:2b"   # FAST + FREE

def call_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=30   # 🔥 reduced from 120s
    )
    return response.json().get("response", "")
