from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_results(
    query,
    results,
    preferences=""
):

    result_text = []

    for item in results:

        metadata = item.get("metadata", {})

        result_text.append(
            f"""
Title: {item.get("title","")}

Source: {item.get("source","")}

Description:
{(item.get("description","") or "")[:300]}

URL:
{item.get("url","")}

Metadata:
{metadata}

Score:
{item.get("score",0)}
"""
        )

    result_text = "\n---------------------------\n".join(result_text)

    prompt = f"""
You are an AI Research Resource Recommender.

The user may ask for:

- GitHub repositories
- Documentation
- Research papers
- Datasets
- Blogs
- StackOverflow discussions

User Query:
{query}

User Preferences:
{preferences}

Candidate Results:

{result_text}

Instructions:

1. Consider ONLY the provided results.
2. Rank them according to relevance.
3. Respect user preferences.
4. Explain why each result is useful.
5. Mention the source type.
6. If nothing is relevant, clearly say:
   "No relevant resources found."
7. Do not invent resources.
8. At the beginning, provide an Overall Match Score (0-100).

Return the answer in this format:

Overall Match Score: XX%

1.

Title:

Source:

Match Score:

Reason:

URL:

2.

Title:

Source:

Match Score:

Reason:

URL:
"""

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    return response.choices[0].message.content