from fastapi import FastAPI
from pydantic import BaseModel

from agent.workflow import workflow

from memory.feedback_store import add_feedback
from memory.history_store import (
    save_response_version,
    get_latest_response
)
from memory.evaluator import compare_versions

app = FastAPI()


class QueryRequest(BaseModel):
    query: str
    sources: list[str] = ["github"]
    website: str | None = None


class FeedbackRequest(BaseModel):
    query: str
    feedback: str


@app.post("/search")
def search(req: QueryRequest):

    result = workflow.invoke({

        "user_query": req.query,

        "selected_sources": ["github"],
        "website": "",

        "search_results": [],

        "final_answer": "",

        "feedback": ""
    })

    answer = result["final_answer"]

    version = save_response_version(
        query=req.query,
        response=answer,
        preferences=""
    )

    return {
    "version": version,
    "results": result["search_results"],
    "answer": answer
    }


@app.post("/feedback")
def save_feedback(req: FeedbackRequest):

    previous = get_latest_response(
        req.query
    )

    if not previous:

        return {
            "error":
            "No previous recommendation found for this query. Run /search first."
        }

    previous_response = previous["response"]

    add_feedback(
        req.query,
        req.feedback
    )

    workflow.invoke({
    "user_query": req.query,
    "selected_sources": ["github"],
    "website": "",
    "search_results": [],
    "final_answer": "",
    "feedback": ""
})

    new_response = result["final_answer"]

    new_version = save_response_version(
        query=req.query,
        response=new_response,
        preferences=req.feedback
    )

    evaluation = compare_versions(
        preference_text=req.feedback,
        previous_response=previous_response,
        new_response=new_response
    )

    return {

        "message":
            "Feedback saved and recommendation regenerated",

        "previous_version":
            previous["version"],

        "new_version":
            new_version,

        "pas":
            evaluation,

        "updated_recommendation":
            new_response
    }