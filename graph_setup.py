from langgraph.graph import StateGraph
from nodes.search_node import search_node
from nodes.summarize_node import summarize_node
from nodes.chroma_node import chroma_node
from typing import TypedDict

class GraphState(TypedDict):
    query: str
    web_results: str
    pdf_results: str
    report: str


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("search", search_node)
    graph.add_node("chroma", chroma_node)
    graph.add_node("summarize", summarize_node)

    graph.set_entry_point("search")
    graph.add_edge("search", "chroma")
    graph.add_edge("chroma", "summarize")
    graph.set_finish_point("summarize")
    
    compiled = graph.compile()
    return compiled
