import json
from pathlib import Path
from datetime import datetime

import numpy as np

from memory.embeddings import get_embedding


FILE = Path("memory/feedbacks.json")

# Better for short technical queries
SIMILARITY_THRESHOLD = 0.70

TOP_K = 3


def load_feedbacks():

    if not FILE.exists():
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_feedbacks(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def cosine_similarity(v1, v2):

    v1 = np.array(v1)
    v2 = np.array(v2)

    return float(np.dot(v1, v2))


def add_feedback(
        query,
        feedback
):

    print("\n========== ADD FEEDBACK ==========")
    print("New Query:", query)
    print("Feedback :", feedback)

    records = load_feedbacks()

    query_embedding = get_embedding(query)

    for record in records:

        similarity = cosine_similarity(
            query_embedding,
            record["embedding"]
        )

        print(
            f"Similarity with "
            f"'{record['query']}' = "
            f"{similarity:.3f}"
        )

        if similarity >= SIMILARITY_THRESHOLD:

            print(
                f"Updating existing memory -> "
                f"{record['query']}"
            )

            old_feedback = record["feedback"]

            # Prevent duplicates
            if feedback.lower() not in old_feedback.lower():

                record["feedback"] = (
                    old_feedback
                    + " | "
                    + feedback
                )

            record["updated_at"] = (
                datetime.utcnow()
                .isoformat()
            )

            save_feedbacks(records)

            return

    print(
        f"Creating new memory -> {query}"
    )

    records.append({

        "query":
            query,

        "embedding":
            query_embedding,

        "feedback":
            feedback,

        "updated_at":
            datetime.utcnow()
            .isoformat()
    })

    save_feedbacks(records)


def get_relevant_feedback(
        current_query
):

    print("\n========== RETRIEVAL ==========")

    records = load_feedbacks()

    if not records:

        print("No feedback records found.")

        return ""

    current_embedding = get_embedding(
        current_query
    )

    scored = []

    for record in records:

        similarity = cosine_similarity(
            current_embedding,
            record["embedding"]
        )

        print(
            f"Similarity with "
            f"'{record['query']}' = "
            f"{similarity:.3f}"
        )

        if similarity >= SIMILARITY_THRESHOLD:

            scored.append(
                (
                    similarity,
                    record["feedback"]
                )
            )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    top_feedbacks = [
        item[1]
        for item in scored[:TOP_K]
    ]

    print(
        "\nCurrent Query:",
        current_query
    )

    print(
        "Matched Feedback:",
        top_feedbacks
    )

    return "\n".join(
        top_feedbacks
    )