# nodes/chroma_node.py

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

load_dotenv()

CHROMA_DIR = "astro_chroma_db"

vectorstore = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
)

qa_chain = load_qa_chain(
    ChatOpenAI(temperature=0, api_key=os.getenv("OPENAI_API_KEY")),
    chain_type="stuff"
)

def chroma_node(state):
    query = state["query"]
    print(f"📚 Searching Chroma for: {query}")
    docs = vectorstore.similarity_search(query, k=4)
    summary = qa_chain.run(input_documents=docs, question=query)
    state["pdf_results"] = summary
    return state
