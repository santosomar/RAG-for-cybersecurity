# This script demonstrates how to create a Chroma vector store from a text file
# and persist it to disk. The script checks if the vector store already exists
# in the persistent directory and initializes it if it does not exist.

# Instructor: Omar Santos @santosomar

# importing the required libraries
import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI


# Defining the directory containing the relevant data 
# In this example, the text file contains information about SSRF vulnerabilities
# # and attacks.
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "ssrf.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Checking if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensuring that the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Reading the text content from the file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Splitting the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    docs = text_splitter.split_documents(documents)

    # Displaying information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Creating embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    # Creatting the vector store/database
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")
