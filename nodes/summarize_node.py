from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

prompt = PromptTemplate.from_template("""
You are a research assistant. Create a clear and insightful research summary for the topic based on the following:

### Web Search
{web_results}

### PDF Knowledge Base
{pdf_results}

Only include high-quality and relevant points.
""")

summarize_chain = LLMChain(llm=llm, prompt=prompt)

def summarize_node(state):
    report = summarize_chain.run({
        "web_results": state["web_results"],
        "pdf_results": state["pdf_results"]
    })
    state["report"] = report
    return state
