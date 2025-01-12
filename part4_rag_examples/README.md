# Basic RAG Example: Vector Store Creation

This is an example script by Omar Santos that demonstrates how to create and persist a Chroma vector store from a text file using LangChain. It's designed as an educational example for implementing Retrieval-Augmented Generation (RAG) systems.

## Overview

The script performs the following operations:
1. Checks for an existing vector store in the specified persistent directory
2. If no vector store exists, it:
   - Loads a text file containing SSRF (Server-Side Request Forgery) vulnerability information
   - Splits the document into manageable chunks
   - Creates embeddings using OpenAI's embedding model
   - Stores the embeddings in a Chroma vector database

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb
  ```
- OpenAI API key set in your environment variables

## Project Structure

```
part4_rag_examples/
├── basic_rag_part1.py
├── data/
│   └── ssrf.txt         # Text file containing SSRF information
└── db/
    └── chroma_db/       # Directory where the vector store is persisted
```

## Usage

1. Ensure you have your OpenAI API key set:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Place your text data in the `data/ssrf.txt` file

3. Run the script:
   ```bash
   python basic_rag_part1.py
   ```

## Features

- **Automatic Vector Store Initialization**: Only creates a new vector store if one doesn't exist
- **Document Chunking**: Splits large documents into manageable pieces (1000 characters each)
- **Persistent Storage**: Saves the vector store to disk for future use
- **OpenAI Embeddings**: Uses OpenAI's text-embedding-3-small model for creating embeddings

## Notes

- The script uses the `text-embedding-3-small` model from OpenAI
- The chunk size is set to 1000 characters with no overlap
- The vector store is persisted to disk and can be reused in subsequent runs

---

# Basic RAG Example - Part 2: Document Retrieval

This script demonstrates how to retrieve relevant documents from a Chroma vector store using LangChain. It's designed as an educational example for implementing Retrieval-Augmented Generation (RAG) systems.

## Overview

The script performs the following operations:
1. Loads an existing Chroma vector store from a persistent directory
2. Creates embeddings for a user query using OpenAI's embedding model
3. Retrieves relevant documents based on similarity scoring
4. Displays the retrieved documents and their metadata

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb
  ```
- OpenAI API key set in your environment variables
- Existing Chroma vector store (created using Part 1 of this example)

## Usage

1. Ensure you have your OpenAI API key set:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Run the script:
   ```bash
   python basic_rag_part2.py
   ```

## Features

- **Vector Store Loading**: Loads an existing Chroma vector store from disk
- **Similarity Search**: Uses similarity scoring to find relevant documents
- **Threshold-Based Retrieval**: Only returns documents with a similarity score above 0.5
- **Metadata Display**: Shows source information for retrieved documents
- **OpenAI Embeddings**: Uses OpenAI's text-embedding-3-small model for query embedding

## Configuration

- Uses the `text-embedding-3-small` model from OpenAI
- Retrieves up to 5 most relevant documents (k=5)
- Minimum similarity score threshold: 0.5

---

# RAG Example with Document Metadata

This script demonstrates how to create a Chroma vector store with metadata using LangChain. It processes multiple text files and stores them with their source information for enhanced retrieval capabilities.

## Overview

The script performs the following operations:
1. Checks for an existing vector store in the specified persistent directory
2. If no vector store exists, it:
   - Loads all text files from the data directory
   - Adds source metadata to each document
   - Splits documents into manageable chunks
   - Creates embeddings using OpenAI's embedding model
   - Stores the embeddings and metadata in a Chroma vector database

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb
  ```
- OpenAI API key set in your environment variables

## Project Structure

```
part4_rag_examples/
├── rag_basics_metadata_part1.py
├── data/
│   └── *.txt           # Text files to be processed
└── db/
    └── chroma_db_with_metadata/  # Directory where the vector store is persisted
```

## Usage

1. Ensure you have your OpenAI API key set:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Place your text files in the `data/` directory

3. Run the script:
   ```bash
   python rag_basics_metadata_part1.py
   ```

## Features

- **Multiple Document Processing**: Processes all .txt files in the data directory
- **Metadata Tracking**: Stores the source filename as metadata for each document
- **Automatic Vector Store Initialization**: Only creates a new vector store if one doesn't exist
- **Document Chunking**: Splits large documents into manageable pieces (1000 characters each)
- **Persistent Storage**: Saves the vector store to disk for future use
- **OpenAI Embeddings**: Uses OpenAI's text-embedding-3-small model for creating embeddings

## Configuration

- Chunk size: 1000 characters
- No chunk overlap
- Embedding model: text-embedding-3-small
- Supported file format: .txt

## Notes

- The script will raise a FileNotFoundError if the data directory doesn't exist
- Progress messages are printed during vector store creation
- The vector store is only created once; subsequent runs will use the existing store

---


# RAG Example - Metadata-Based Document Retrieval Part 2

This script demonstrates how to retrieve documents with metadata from a Chroma vector store using LangChain. It shows how to perform similarity searches with a score threshold and display both document content and metadata.

## Overview

The script performs the following operations:
1. Loads an existing Chroma vector store containing documents with metadata
2. Performs a similarity search based on a user query
3. Retrieves and displays relevant documents along with their source information

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb
  ```
- OpenAI API key set in your environment variables
- Existing Chroma vector store with metadata (created using the companion creation script)

## Usage

1. Ensure you have your OpenAI API key set:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Run the script:
   ```bash
   python rag_basics_metadata_part2.py
   ```

## Features

- **Metadata-Aware Retrieval**: Retrieves documents with their associated source information
- **Similarity Score Threshold**: Only returns documents with a similarity score above 0.1
- **Limited Results**: Returns up to 3 most relevant documents
- **Source Tracking**: Displays the source file for each retrieved document
- **OpenAI Embeddings**: Uses OpenAI's text-embedding-3-small model for query embedding

## Configuration

- Model: text-embedding-3-small
- Maximum results (k): 3
- Similarity score threshold: 0.1
- Search type: similarity_score_threshold

## Example Query

The script currently searches for:
```python
query = "any are api related hosts?"
```

## Output Format

For each retrieved document, the script displays:
- Document content
- Source file information

---


# Text Splitting Deep Dive

This script demonstrates different text splitting strategies for RAG (Retrieval-Augmented Generation) applications using LangChain. It showcases various splitting methods and their impact on document retrieval.

## Overview

The script demonstrates five different text splitting approaches:
1. Character-based Splitting
2. Sentence-based Splitting
3. Token-based Splitting
4. Recursive Character-based Splitting
5. Custom Splitting

Each splitting method creates its own Chroma vector store, allowing for comparison of retrieval results.

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb sentence-transformers
  ```
- OpenAI API key set in your environment variables

## Project Structure

```
part4_rag_examples/
├── text_splitting_deep_dive.py
├── data/
│   └── tesla.json      # Source document
└── db/
    ├── chroma_db_char/
    ├── chroma_db_sent/
    ├── chroma_db_token/
    ├── chroma_db_rec_char/
    └── chroma_db_custom/
```

## Features

### Splitting Methods

1. **Character-based Splitting**
   - Splits text into fixed-size character chunks
   - Chunk size: 1000 characters
   - Overlap: 100 characters

2. **Sentence-based Splitting**
   - Splits text at sentence boundaries
   - Uses sentence-transformers tokenizer
   - Chunk size: 1000 tokens

3. **Token-based Splitting**
   - Splits text based on token count
   - Chunk size: 512 tokens
   - No overlap

4. **Recursive Character-based Splitting**
   - Splits text at natural boundaries
   - Chunk size: 1000 characters
   - Overlap: 100 characters

5. **Custom Splitting**
   - Example implementation splitting by paragraphs
   - Demonstrates how to create custom splitters

### Vector Store Features

- Persistent storage for each splitting method
- Similarity search with score threshold
- Metadata preservation
- Query results display with source information

## Usage

1. Ensure you have your OpenAI API key set:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

2. Place your source document in `data/tesla.json`

3. Run the script:
   ```bash
   python text_splitting_deep_dive.py
   ```

## Query Example

The script includes a sample query:
```python
query = "What hosts are in Amazon?"
```

This query is executed against all five vector stores, allowing you to compare how different splitting methods affect retrieval results.

## Configuration

- Embedding model: text-embedding-3-small
- Similarity score threshold: 0.1
- Results per query: 1 document
- Search type: similarity_score_threshold

---

# Web Scraping RAG Example

This script demonstrates how to create a RAG (Retrieval-Augmented Generation) system that scrapes web content, processes it, and stores it in a vector database for semantic search capabilities.

## Overview

The script performs the following operations:
1. Scrapes content from specified web pages using WebBaseLoader
2. Splits the content into manageable chunks
3. Creates embeddings using OpenAI's embedding model
4. Stores the embeddings in a Chroma vector database
5. Performs semantic search queries on the stored content

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install langchain langchain-openai chromadb python-dotenv
  ```
- OpenAI API key set in your `.env` file

## Project Structure

```
part4_rag_examples/
├── web_scrape_basic.py
└── db/
    └── chroma_db_secretcorp/  # Directory where the vector store is persisted
```

## Features

- **Web Scraping**: Automatically extracts content from specified URLs
- **Content Processing**: 
  - Splits content into 1000-character chunks
  - No overlap between chunks for efficiency
- **Vector Storage**:
  - Persistent Chroma database
  - Automatic initialization check
  - Source URL metadata preservation
- **Semantic Search**:
  - Similarity-based retrieval
  - Returns top 3 most relevant results
  - Includes source metadata in results

## Usage

1. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. Modify the `urls` list to include your target websites:
   ```python
   urls = ["https://secretcorp.org"]
   ```

3. Run the script:
   ```bash
   python web_scrape_basic.py
   ```

## Configuration

- Embedding model: text-embedding-3-small
- Chunk size: 1000 characters
- Search results: Top 3 most relevant documents
- Search type: similarity

## Example Query

The script includes a sample query:
```python
query = "What is secretcorp all about?"
```

## Output

The script provides:
- Number of document chunks created
- Sample of processed content
- Vector store creation status
- Relevant documents for the query with their sources

## Author

Instructor: Omar Santos (@santosomar)
