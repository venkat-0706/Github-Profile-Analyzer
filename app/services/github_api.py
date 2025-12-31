import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com/users"
TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json"
}

if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"


def fetch_user_data(username: str) -> dict:
    user_resp = requests.get(f"{BASE_URL}/{username}", headers=HEADERS)

    if user_resp.status_code != 200:
        raise ValueError("GitHub user not found or API rate limit exceeded")

    user = user_resp.json()

    repos_resp = requests.get(f"{BASE_URL}/{username}/repos", headers=HEADERS)
    repos = repos_resp.json() if repos_resp.status_code == 200 else []

    stars = 0
    forks = 0
    repo_descriptions = 0

    for repo in repos:
        stars += repo.get("stargazers_count", 0)
        forks += repo.get("forks_count", 0)
        if repo.get("description"):
            repo_descriptions += 1

    return {
        "followers": user.get("followers", 0),
        "bio": bool(user.get("bio")),
        "blog": bool(user.get("blog")),
        "repos": len(repos),
        "repo_descriptions": repo_descriptions,
        "stars": stars,
        "forks": forks,
    }
