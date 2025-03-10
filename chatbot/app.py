from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'Hello! How can I help you today?'),
        ('user', 'I need help with my computer. It is not turning on.'),
    ]
)

# Streamlit framework
st.title("Chatbot")
input_text = st.text_input("Enter your message")

# openai LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", max_tokens=100)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))