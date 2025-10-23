import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

# Folder where your PDFs are stored
PDF_FOLDER = "data/pdf_data"
# Folder where vector store will be persisted
CHROMA_DIR = "astro_chroma_db"

def load_and_save_to_chroma():
    all_docs = []

    # Load all PDFs in the folder
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER, file)
            print(f"Loading: {file_path}")
            loader = PyPDFLoader(file_path)
            all_docs.extend(loader.load())

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    docs = splitter.split_documents(all_docs)

    # Create Chroma vector store
    print("Creating ChromaDB...")
    Chroma.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY")),
        persist_directory=CHROMA_DIR,
    )
    print("Done. Chroma vector store saved at:", CHROMA_DIR)

if __name__ == "__main__":
    load_and_save_to_chroma()
