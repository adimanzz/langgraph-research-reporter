from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

search_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_node(state):
    query = state["query"]
    print(f"Searching the web for topic: {query}")
    results = search_client.search(query, search_depth='advanced', include_answer=True)
    state["search_results"] = results["answer"]
    return state