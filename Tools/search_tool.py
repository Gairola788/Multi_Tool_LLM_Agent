from langchain.tools import tool
import requests

@tool
def search_agent(query):
    """Search the internet for general information or facts.
Use this when the question requires knowledge from the web."""
    
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    response = requests.get(url)
    data = response.json()
    
    return data["AbstractText"] if data["AbstractText"] else "No result found."