from langgraph.graph import StateGraph

from agent.state import AgentState

from agent.research_agent import (
    search_node,
    scoring_node,
    ranking_node
)

builder = StateGraph(AgentState)

builder.add_node(
    "search",
    search_node
)

builder.add_node(
    "scoring",
    scoring_node
)

builder.add_node(
    "ranking",
    ranking_node
)

builder.add_edge(
    "search",
    "scoring"
)

builder.add_edge(
    "scoring",
    "ranking"
)

builder.set_entry_point("search")

workflow = builder.compile()