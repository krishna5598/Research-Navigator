import json

from pathlib import Path

from datetime import datetime


FILE = Path("memory/recommendation_history.json")


def load_history():

    if not FILE.exists():
        return []

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_history(data):

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


def get_latest_version(query):

    history = load_history()

    versions = [

        item["version"]

        for item in history

        if item["query"] == query
    ]

    if not versions:
        return 0

    return max(versions)


def save_response_version(
        query,
        response,
        preferences=""
):

    history = load_history()

    latest_version = get_latest_version(
        query
    )

    new_version = (
        latest_version + 1
    )

    history.append({

        "query":
            query,

        "version":
            new_version,

        "response":
            response,

        "preferences":
            preferences,

        "timestamp":
            datetime.utcnow()
            .isoformat()
    })

    save_history(history)

    return new_version


def get_latest_response(query):

    history = load_history()

    matching = [

        item

        for item in history

        if item["query"] == query
    ]

    if not matching:
        return None

    latest = max(
        matching,
        key=lambda x: x["version"]
    )

    return latest


def get_query_history(query):

    history = load_history()

    matching = [

        item

        for item in history

        if item["query"] == query
    ]

    matching.sort(
        key=lambda x: x["version"]
    )

    return matching


def get_previous_response(query):

    history = get_query_history(
        query
    )

    if len(history) < 2:
        return None

    return history[-2]


def clear_history():

    save_history([])

    print(
        "Recommendation history cleared."
    )