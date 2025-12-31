from app.services.score_engine import calculate_score

def test_score_limits():
    data = {
        "followers": 100,
        "repos": 10,
        "repo_descriptions": 5,
        "stars": 50,
        "forks": 20,
        "bio": True,
        "blog": False,
    }

    score, metrics, _ = calculate_score(data)
    assert score <= 100
    assert score > 0
