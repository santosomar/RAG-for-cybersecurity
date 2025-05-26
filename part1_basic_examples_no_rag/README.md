# Basic LangChain OpenAI Chat Example

This folder contains a basic example demonstrating how to use LangChain with OpenAI's chat models without Retrieval Augmented Generation (RAG).

## Overview

The example shows how to:
- Set up a basic chat interaction with OpenAI's models through LangChain
- Load environment variables securely
- Create and invoke a chat model
- Handle and display model responses

## Files

- `chat_model_basic.py`: Basic implementation of chat functionality using LangChain and OpenAI

## Prerequisites

- Python 3.x
- Required packages:
  - `langchain`
  - `langchain-openai`
  - `python-dotenv`

## Setup

1. Install the required packages:

```bash
pip install langchain langchain-openai python-dotenv
```

2. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the example script:
```bash
python chat_model_basic.py
```

The script will:
1. Load your OpenAI API key from the environment
2. Initialize a chat model (gpt-4.1-mini)
3. Send a query about Retrieval Augmented Generation in Cybersecurity
4. Display both the full response object and its content

## Notes

- The example uses the "gpt-4.1-mini" model, but you can modify this to use other OpenAI models
- Make sure to keep your API key secure and never commit it to version control
- This is a basic example without RAG capabilities - see other examples for more advanced features


## Additional Resources

- [LangChain Chat Model Documentation](https://python.langchain.com/v0.2/docs/integrations/chat/)
- [OpenAI Chat Model Documentation](https://python.langchain.com/v0.2/docs/integrations/chat/openai/)


## Files

- `chat_model_basic.py`: Basic implementation of chat functionality using LangChain and OpenAI
- `embeddings.py`: Demonstrates how to generate text embeddings using OpenAI's embedding models

## Examples

### Chat Model Example
Basic chat interaction with OpenAI models through LangChain.

### Embeddings Example
The `embeddings.py` script shows how to:
- Generate embeddings for text input using OpenAI's API
- Use the "text-embedding-3-small" model
- Process and display embedding vectors

Example usage:
```bash
python embeddings.py
```



## Streamlit Interface

The chatbot example includes a Streamlit web interface that provides:
- A clean, interactive chat interface
- Real-time streaming responses
- Persistent chat history within the session
- Easy-to-use input field for questions

To run the Streamlit interface: 
```bash
streamlit run chatbot_example.py
```


## Security Considerations

### API Key Management
- API keys are loaded from environment variables using python-dotenv
- Never hardcode API keys in your source code
- Add `.env` to your `.gitignore` file

### Best Practices
- Regularly rotate your API keys
- Monitor API usage for unusual patterns
- Implement rate limiting for production deployments
- Validate and sanitize user inputs

## Part 1Project Structure

- `chat_model_basic.py`: Basic implementation of chat functionality using LangChain and OpenAI
- `embeddings.py`: Demonstrates how to generate text embeddings using OpenAI's embedding models
- `chatbot_example.py`: Streamlit interface for the chatbot example
- `.env`: Environment variables file for API keys
- `requirements.txt`: List of required packages

