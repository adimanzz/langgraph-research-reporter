from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

prompt = PromptTemplate.from_template("""
YYou are a research assistant. Based on the following information, create a clear, concise, and insightful research summary on the given topic. The summary should follow this structure:

1. **Introduction**  
   Briefly introduce the topic, its context, and its relevance.

2. **Key Findings**  
   Present the most important insights and evidence. Organize the findings logically and concisely. Use bullet points or paragraphs where appropriate.

3. **Future Outlook**  
   Discuss implications, open questions, or directions for future research.

Include citations and references wherever applicable. Only include information that is accurate, high-quality, and directly relevant to the topic.

---

### Web Search Results
{web_results}

### PDF Knowledge Base
{pdf_results}
""")

summarize_chain = LLMChain(llm=llm, prompt=prompt)

def summarize_node(state):
    report = summarize_chain.run({
        "web_results": state["web_results"],
        "pdf_results": state["pdf_results"]
    })
    state["report"] = report
    return state
