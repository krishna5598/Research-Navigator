import numpy as np

from memory.embeddings import get_embedding


def cosine_similarity(v1, v2):

    v1 = np.array(v1)
    v2 = np.array(v2)

    return float(np.dot(v1, v2))


def calculate_pas(
        preference_text,
        response_text
):

    if not preference_text:
        return 0.0

    preference_embedding = get_embedding(
        preference_text
    )

    response_embedding = get_embedding(
        response_text
    )

    score = cosine_similarity(
        preference_embedding,
        response_embedding
    )

    return round(score, 4)


def compare_versions(
        preference_text,
        previous_response,
        new_response
):

    before_score = calculate_pas(
        preference_text,
        previous_response
    )

    after_score = calculate_pas(
        preference_text,
        new_response
    )

    improvement = (
        after_score -
        before_score
    )

    return {

        "before":
            round(
                before_score,
                4
            ),

        "after":
            round(
                after_score,
                4
            ),

        "improvement":
            round(
                improvement,
                4
            ),

        "improved":
            after_score >
            before_score
    }