# This script demonstrates how to use the LangChain Community VectorStores module to retrieve relevant documents based on a user's question.

# Instructor: Omar Santos @santosomar 

# importing the required libraries
import os

from langchain_chroma import Chroma 
from langchain_openai import OpenAIEmbeddings

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_security")

# Define the embedding model (in this case, OpenAI's text-embedding-3-small. 
# Note: You can also use other embedding models such as HuggingFace's SentenceTransformers, Cohere, or any other embedding model that is more appropriate for your use case. Refer to the "Selecting Embedding Models" white paper at https://sec.cloudapps.cisco.com/security/center/resources/selecting-embedding-models for some tips on selecting an embedding model.)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the user's question
query = "What is SSRF? Provide an example of an SSRF attack."

# Retrieve relevant documents based on the query
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 5, "score_threshold": 0.5},
)
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")
