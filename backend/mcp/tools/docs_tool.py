import requests

DOC_SITES = {
    "pytorch": "https://pytorch.org/docs/stable/",
    "tensorflow": "https://www.tensorflow.org",
    "fastapi": "https://fastapi.tiangolo.com",
    "langchain": "https://python.langchain.com",
    "huggingface": "https://huggingface.co/docs",
    "react": "https://react.dev",
    "python": "https://docs.python.org/3"
}


def search_docs(query: str, website: str = ""):

    results = []

    q = query.lower()

    for name, url in DOC_SITES.items():

        if name in q:

            results.append({

                "title": f"{name.title()} Documentation",

                "url": url,

                "description": f"Official {name} documentation",

                "source": "docs",

                "metadata": {
                    "official": True
                }

            })

    return results