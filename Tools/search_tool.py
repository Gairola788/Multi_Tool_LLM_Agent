from langchain.tools import tool
import requests

@tool
def search_agent(query):
    """Search any query regarding any topic like for ex:What is meaning of Inflation,or any domain related topic,
    args: any keyword"""
    
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    response = requests.get(url)
    data = response.json()
    
    return data["AbstractText"] if data["AbstractText"] else "No result found."