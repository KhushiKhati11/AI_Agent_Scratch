from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama

import os

load_dotenv()

llm = ChatOllama(model="mistral")

try:
    response = llm.invoke("What is python?")
    print(response.content)  # Assuming response.content contains the text output
except Exception as e:
    print(f"Error during model invocation: {e}")