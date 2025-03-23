from langchain_anthropic import ChatAnthropic
from browser_use import Agent

import asyncio

# Initialize the model
llm = ChatAnthropic(
    model_name="claude-3-7-sonnet-20250219",
    temperature=0.0,
    timeout=100, # Increase for complex tasks
)

# Create agent with the model
async def main():
    agent = Agent(
        task="""
        Google のサイト https://www.google.com を開いて
        Google CloudとAWSを客観的に検索して比較して"
        """,
        llm=llm
    )

    result = await agent.run()
    print(result)

asyncio.run(main())