from langchain.agents import create_agent

from tools.calculator import calculator
from prompts.system_prompt import SYSTEM_PROMPT

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain.agents.middleware import ProviderToolSearchMiddleware

load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')
model = ChatGroq(
    groq_api_key= GROQ_API_KEY,
    model="llama-3.1-8b-instant")


agent = create_agent(
  model,
  tools=[calculator],
  system_prompt=SYSTEM_PROMPT,
  middleware=[
    ProviderToolSearchMiddleware(
      searchable_tools=['calculator']
    )
  ]
)

