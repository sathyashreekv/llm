from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from datetime import datetime
import random

load_dotenv()

def get_current_time() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[get_current_time],
        markdown=False
    )
