from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

github = Github(os.getenv("GITHUB_TOKEN"))


def search_github(query: str, website: str = ""):

    print(f"\nSearching GitHub : {query}")

    repositories = github.search_repositories(query)

    results = []

    for repo in repositories[:10]:

        results.append(
            {
                "title": repo.full_name,
                "url": repo.html_url,
                "description": repo.description or "",
                "source": "repo",
                "metadata": {
                    "stars": repo.stargazers_count
                }
            }
        )

    return results