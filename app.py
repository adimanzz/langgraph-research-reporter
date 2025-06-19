from langgraph.graph import StateGraph
from nodes.search_node import search_node
from nodes.summarize_node import summarize_node
from typing import TypedDict

class GraphState(TypedDict):
    query: str
    search_results: str
    report: str


# Define nodes
graph = StateGraph(GraphState)

graph.add_node("search", search_node)
graph.add_node("summarize", summarize_node)

# Define flow
graph.set_entry_point("search")
graph.add_edge("search", "summarize")
graph.set_finish_point("summarize")


compiled = graph.compile()
query = input("Enter your research topic: ")
results = compiled.invoke({"query": query})
print("\n ====== Final Report ====== \n")
print(results['report'])

