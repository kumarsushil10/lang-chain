from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import os
import uvicorn
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv



load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

app = FastAPI(
    title="Langchain Server API",
    description="simple API for langchain",
    version="0.1"
)

model = OllamaLLM(model="llama3.2")
chatprompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'Hello! How can I help you today?'),
        ('user', "Question:{question}"),
    ]
)

add_routes(
    app,
    chatprompt | model,
    path="/ollama",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)
