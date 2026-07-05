from langchain.agents import create_agent

from tools import TOOLS
from prompts.system_prompt import SYSTEM_PROMPT

import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

model = ChatGoogleGenerativeAI(
  model = 'gemini-2.5-flash',
  temperature = 0,
)

agent = create_agent(
  model,
  tools=TOOLS,
  system_prompt=SYSTEM_PROMPT,
)

