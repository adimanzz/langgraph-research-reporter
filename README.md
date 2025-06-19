# LangGraph Research Reporter

A multi-agent research tool using LangGraph, Tavily, and OpenAI to generate structured reports based on web search results.

## How It Works
1. Takes a user query (e.g. "Biomass in Alberta")
2. Searches the web via Tavily
3. Summarizes with OpenAI
4. Outputs a structured research report

## Setup

```bash
pip install langgraph langchain-openai tavily-python python-dotenv
