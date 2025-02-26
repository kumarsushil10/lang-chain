from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM  # Updated import
import streamlit as st
import os
from dotenv import load_dotenv
from ollama._types import ResponseError

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'Hello! How can I help you today?'),
        ('user', "Question:{question}"),
    ]
)

# Streamlit framework
st.title("Chatbot llama 3.2")
input_text = st.text_input("Enter your message")

# ollama llama 3.2 LLM
llm = OllamaLLM(model="llama3.2")  # Updated usage
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({'question': input_text})
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")