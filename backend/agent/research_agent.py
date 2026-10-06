from mcp.client import MCPClient

from llm.groq_client import analyze_results

from agent.scoring import rank_results

from memory.feedback_store import (
    add_feedback,
    get_relevant_feedback
)

client = MCPClient()


def search_node(state):

    query = state["user_query"]

    sources = state.get("selected_sources", [])

    website = state.get("website", "")

    print("\n========== SEARCH NODE ==========")
    print("Query:", query)
    print("Sources:", sources)
    print("Website:", website)

    all_results = []

    for source in sources:

        print(f"\nSearching source: {source}")

        try:

            results = client.search(
                source=source,
                query=query,
                website=website
            )

            print(
                "Results returned:",
                len(results) if results else 0
            )

            if results:
                print("First result:", results[0])
                all_results.extend(results)

        except Exception as e:

            print(f"{source} search failed: {e}")

    print("\n========== SEARCH COMPLETE ==========")
    print("TOTAL RESULTS:", len(all_results))

    state["search_results"] = all_results

    return state


def scoring_node(state):

    ranked = rank_results(
        state["search_results"],
        state["user_query"]
    )

    state["search_results"] = ranked[:3]

    return state


def ranking_node(state):

    preferences = get_relevant_feedback(
        state["user_query"]
    )

    answer = analyze_results(
        query=state["user_query"],
        results=state["search_results"],
        preferences=preferences
    )

    state["final_answer"] = answer

    return state


def feedback_node(state):

    feedback = state.get("feedback", "")

    if feedback:

        add_feedback(
            state["user_query"],
            feedback
        )

    return state