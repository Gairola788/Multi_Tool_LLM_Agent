from langchain.tools import tool
import requests

@tool
def search_agent(query: str):
    """Search the internet for general information."""

    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    try:
        response = requests.get(url)

        if response.status_code not in [200, 202]:
            return {"error": f"HTTP Error: {response.status_code}"}

        data = response.json()

        abstract = data.get("AbstractText")
        related = data.get("RelatedTopics", [])

        # ✅ Primary result
        if abstract:
            return {
                "query": query,
                "result": abstract,
                "source": "abstract"
            }

        # ✅ Fallback to related topics
        for item in related:
            if isinstance(item, dict) and item.get("Text"):
                return {
                    "query": query,
                    "result": item["Text"],
                    "source": "related"
                }

        return {"error": "No useful result found"}

    except Exception as e:
        return {"error": str(e)}