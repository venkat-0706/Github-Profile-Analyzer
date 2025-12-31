from app.services.metrics_calculator import calculate_metrics


def test_calculate_metrics_basic():
    """
    Test whether metrics are calculated correctly
    and stay within expected bounds.
    """

    fake_cleaned_data = {
        "followers": 50,
        "repo_count": 10,
        "repo_descriptions": 7,
        "stars": 120,
        "forks": 30,
        "bio": True,
        "email": False,
        "company": True,
        "location": True,
        "blog": False,
    }

    metrics, diagnostics = calculate_metrics(fake_cleaned_data)

    # Metrics existence
    assert "user_popularity" in metrics
    assert "repository_quality" in metrics
    assert "impact" in metrics
    assert "profile_strength" in metrics
    assert "repo_count" in metrics

    # Metrics boundaries
    for value in metrics.values():
        assert value >= 0
        assert value <= 20 or value <= 40  # based on design

    # Diagnostics check
    assert diagnostics["followers"] == 50
    assert diagnostics["repositories"] == 10
