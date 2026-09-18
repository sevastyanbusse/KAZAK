import os

from dotenv import load_dotenv
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import DuckDuckGoSearchRun
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

#loads the Python environment
load_dotenv()

#creates the Ollama model

model = OllamaLLM (
  model="llama3.1",
  temperature=0.7,
  num_predict=256
)

  
