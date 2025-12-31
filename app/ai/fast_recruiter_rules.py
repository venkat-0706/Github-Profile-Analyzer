def fast_recruiter_suggestions(drawbacks: list) -> list:
    suggestions = []

    for d in drawbacks:
        if "follower" in d:
            suggestions.append(
                "Increase visibility; recruiters often prioritize profiles with community traction."
            )
        elif "repositories" in d:
            suggestions.append(
                "Recruiters expect multiple projects to evaluate consistency and depth."
            )
        elif "descriptions" in d:
            suggestions.append(
                "Clear documentation helps recruiters quickly assess project relevance."
            )
        elif "engagement" in d:
            suggestions.append(
                "Stars and forks act as social proof of real-world value."
            )
        elif "bio" in d:
            suggestions.append(
                "A concise bio gives recruiters immediate context about your expertise."
            )
        elif "portfolio" in d:
            suggestions.append(
                "External links help recruiters validate skills beyond GitHub."
            )

    return suggestions
