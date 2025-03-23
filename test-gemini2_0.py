from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from browser_use.controller.service import Controller
from browser_use.browser.browser import Browser, BrowserConfig
from pydantic import SecretStr
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

from pydantic import BaseModel
# Define the output format as a Pydantic model
class Shoplist(BaseModel):
	name: str
	yen: int

controller = Controller(output_model=Shoplist)

# Initialize the model
llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash-exp',
        api_key=SecretStr(os.getenv('GEMINI_API_KEY')),
        controller=controller,
    )

task = ""
with open("task.txt") as f:
    task = f.read()

browser = Browser(
	config=BrowserConfig(
		headless=True
        # 注意：デバッグモードでブラウザを開くためには、既存のブラウザを閉じる必要があります。
		# chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # Edgeでも使用可能です。
		# chrome_instance_path='/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
	)
)

# Create agent with the model
async def main():
    agent = Agent(
        task=task,
        browser=browser,
        llm=llm,
    )

    result = await agent.run()
    return result
    # print(result)

asyncio.run(main())
