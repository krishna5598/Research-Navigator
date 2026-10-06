def calculate_relevance(query: str, result: dict):

    query_words = set(query.lower().split())

    metadata = result.get("metadata", {})

    text = (
        str(result.get("title", "")) + " " +
        str(result.get("description", "")) + " " +
        str(metadata)
    ).lower()

    matches = sum(
        1
        for word in query_words
        if word in text
    )

    return matches


def score_result(result: dict, query: str):

    relevance = calculate_relevance(query, result)

    source = result.get("source", "")

    metadata = result.get("metadata", {})

    popularity = 0

    if source == "repo":
        popularity = metadata.get("stars", 0) * 0.01

    elif source == "paper":
        popularity = metadata.get("citations", 0) * 0.02

    elif source == "dataset":
        popularity = metadata.get("downloads", 0) * 0.001

    elif source == "blog":
        popularity = metadata.get("likes", 0) * 0.01

    elif source == "stackoverflow":
        popularity = metadata.get("votes", 0) * 0.05

    score = relevance * 100 + popularity

    result["score"] = round(score, 2)

    return result


def rank_results(results: list, query: str):

    scored = [
        score_result(result, query)
        for result in results
    ]

    ranked = sorted(
        scored,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked