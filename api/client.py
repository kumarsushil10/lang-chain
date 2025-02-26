import requests
import streamlit as st


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/ollama/invoke",
    json = {
        'input':{
            'question':input_text
            }
        })
    return response.json()['output']

st.title("Chatbot olama ")
input_text = st.text_input("Ask any thing..")


if input_text:
    st.write(get_ollama_response(input_text))
    