def calculate_score(data: dict):
    metrics = {
        "Popularity": min(data.get("followers", 0) / 10, 20),
        "Repositories": min(data.get("repos", 0), 20),
        "Repo Quality": min(data.get("repo_descriptions", 0) * 2, 20),
        "Impact": min((data.get("stars", 0) + data.get("forks", 0)) / 10, 20),
        "Profile": 20 if data.get("bio") or data.get("blog") else 0,
    }

    total_score = round(min(sum(metrics.values()), 100), 2)

    diagnostics = {
        "Followers": data.get("followers", 0),
        "Repositories": data.get("repos", 0),
        "Stars": data.get("stars", 0),
        "Forks": data.get("forks", 0),
    }

    return total_score, metrics, diagnostics
