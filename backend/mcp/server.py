from mcp.server.fastmcp import FastMCP
from tools.github_tool import search_github

mcp = FastMCP("Research Navigator")


@mcp.tool()
def github_search(query: str):
    return search_github(query)


if __name__ == "__main__":
    mcp.run()