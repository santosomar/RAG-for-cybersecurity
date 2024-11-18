__author__ = "Omar Santos @santosomar"
__version__ = "0.1.0"
__license__ = "MIT"
__description__ = "A simple chatbot example using LangChain and OpenAI"

# Importing the necessary libraries
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file or from environment variables in the user's machine

load_dotenv()

# Setting up the Streamlit app 
st.title("Omar's Cybersecurity Chatbot")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Creating a chat input for the user to ask questions
if prompt := st.chat_input("Hi Omar, how can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})