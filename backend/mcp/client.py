from mcp.registry import TOOLS


class MCPClient:

    def search(self, source: str, query: str, website: str = ""):

        if source not in TOOLS:
            return []

        return TOOLS[source](query, website)