# 🔎 Research Navigator

> An AI-powered research resource discovery and recommendation system built with **LangGraph, MCP, GitHub Search, Groq LLM, intelligent ranking, and feedback-based memory**.

Research Navigator helps users find relevant technical resources such as GitHub repositories, research papers, datasets, documentation, and other developer resources from a single natural-language query.

The system retrieves candidate resources, ranks them according to the user's query, and uses an LLM to generate concise, explainable recommendations.

---

## 🚀 Key Features

- 🔍 **Intelligent Resource Search**
  - Search technical resources using natural-language queries.
  - Currently integrated with GitHub repository search.

- 🤖 **Agent-Based Architecture**
  - Uses LangGraph to orchestrate the research workflow.
  - Separates searching, scoring, ranking, and recommendation generation.

- 🔌 **MCP-Based Tool Architecture**
  - Modular tool registry allows new research sources to be added easily.
  - GitHub is currently implemented as the first search source.

- 📊 **Repository Ranking**
  - Candidate repositories are scored according to query relevance.
  - The system selects the top relevant repositories before generating the final response.

- 🧠 **LLM-Powered Recommendations**
  - Uses Groq-hosted LLMs to analyze ranked resources.
  - Generates explanations and match scores.

- 💬 **Feedback-Based Memory**
  - Stores user feedback from previous recommendations.
  - Retrieves relevant preferences for future recommendations.

- 🔄 **Recommendation Versioning**
  - Stores previous recommendation versions.
  - Allows feedback-driven regeneration and comparison.

- 🌐 **REST API**
  - FastAPI backend exposes the research agent through API endpoints.
  - Designed for integration with a React frontend.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────┐
                         │   React Frontend │
                         └────────┬─────────┘
                                  │
                                  │ REST API
                                  ▼
                         ┌──────────────────┐
                         │     FastAPI      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    LangGraph     │
                         │  Agent Workflow  │
                         └────────┬─────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  │               │               │
                  ▼               ▼               ▼
             Search Node     Scoring Node    Ranking Node
                  │               │               │
                  ▼               ▼               │
             MCP Client       Ranking Engine       │
                  │                               │
                  ▼                               ▼
             MCP Registry                    Groq LLM
                  │                               │
                  ▼                               ▼
             GitHub Tool                 Final Recommendation
                  │
                  ▼
             GitHub API

                    ┌──────────────────────┐
                    │  Feedback & Memory   │
                    │  Recommendation DB   │
                    └──────────────────────┘
