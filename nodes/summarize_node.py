from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

def summarize_node(state):
    context = state['search_results']
    query = state['query']
    prompt = f"""

You are a research assistant. Based on the following context and query generate a short detailed report.
It should have this format:

## Introduction
## Key Findings
## Recommendations

Query: {query}

Context:
{context}

"""
    print("Generating report...")
    results = llm.predict(prompt)
    state["report"] = results
    return state