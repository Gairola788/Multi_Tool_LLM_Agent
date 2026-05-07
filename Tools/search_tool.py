from langchain.tools import tool
import requests


@tool
def search_agent(query: str):
    """
    Search the internet for general information or facts.
    """

    try:
        url = "https://api.duckduckgo.com/"

        params = {
            "q": query,
            "format": "json"
        }

        response = requests.get(url, params=params)

        # Raise error if bad response
        response.raise_for_status()

        data = response.json()

        # Safe extraction
        result = data.get("AbstractText")

        if result:
            return result

        # fallback topic
        related = data.get("RelatedTopics")

        if related and len(related) > 0:
            first = related[0]

            if isinstance(first, dict):
                return first.get("Text", "No useful result found")

        return "No useful result found"

    except requests.exceptions.RequestException as e:
        return f"HTTP Error: {str(e)}"

    except Exception as e:
        return f"Search Error: {str(e)}"

# from langchain.tools import tool
# import requests

# @tool
# def search_agent(query: str):
#     """Search the internet for general information."""

#     url = f"https://api.duckduckgo.com/?q={query}&format=json"

#     try:
#         response = requests.get(url)

#         if response.status_code not in [200, 202]:
#             return {"error": f"HTTP Error: {response.status_code}"}

#         data = response.json()

#         abstract = data.get("AbstractText")
#         related = data.get("RelatedTopics", [])

#         # ✅ Primary result
#         if abstract:
#             return {
#                 "query": query,
#                 "result": abstract,
#                 "source": "abstract"
#             }

#         # ✅ Fallback to related topics
#         for item in related:
#             if isinstance(item, dict) and item.get("Text"):
#                 return {
#                     "query": query,
#                     "result": item["Text"],
#                     "source": "related"
#                 }

#         return {"error": "No useful result found"}

#     except Exception as e:
#         return {"error": str(e)}