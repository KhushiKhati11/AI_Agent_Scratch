from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from prompt_manager import PromptManager, PromptTool
from langchain.agents import initialize_agent,AgentType

import os

load_dotenv()

llm = ChatOllama(model="mistral")

# try:
#     response = llm.invoke("hello how are you?")
#     print(response.content)  # Assuming response.content contains the text output
# except Exception as e:
#     print(f"Error during model invocation: {e}")

prompt_manager=PromptManager(
    input_variables = ["question"],
    template = "Answer the following question in a concise way:\n{question}"
)
# setting up the tool
prompt_tool = PromptTool(prompt_manager=prompt_manager)

#setting up the agent
agent = initialize_agent(
    tools=[prompt_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

ques = "What is the capital of france?"
# Question format description
try:
    formatted_prompt = prompt_manager.format_prompt(question=ques)
    print(f"Formatted Prompt:{formatted_prompt}")
except Exception as e:
    print(f"Error during model invocation: {e}")

#Invoking agent
response = agent(
    {"input" : ques},
)
print(response["output"])
