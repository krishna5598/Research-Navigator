from mcp.tools.github_tool import search_github

results = search_github("machine learning")

print("\nTOTAL RESULTS:", len(results))

for result in results:
    print(result)