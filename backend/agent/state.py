from typing import TypedDict


class AgentState(TypedDict):

    user_query: str

    selected_sources: list[str]

    website: str

    search_results: list

    final_answer: str

    feedback: str