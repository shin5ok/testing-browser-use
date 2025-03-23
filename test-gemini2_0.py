from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

task = ""
with open("task.txt") as f:
    task = f.read()

print(task)

# Create agent with the model
async def main():
    agent = Agent(
        task=task,
        llm=llm
    )

    result = await agent.run()
    # print(result)

asyncio.run(main())
