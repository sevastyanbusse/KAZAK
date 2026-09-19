#Dependencies need to be installed to run lang-chain

import os 
from dotenv import load_dotenv
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import DuckDuckGoSearchRun
