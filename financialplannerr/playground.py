from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground,serve_playground_app

load_dotenv()
phi.api =  os.getenv('PHIDATA')


##Web Search Agent
web_search_agent = Agent(
    name ='Web Search Agent',
    role='Search the web for the information',
    model=OpenAIChat(id='gpt-3.5-turbo'),
    tools =[DuckDuckGo()],
    instructions =['Always include sources'],
    show_tools_calls=True,
    markdown=True
)


##FInancial Agent
finance_agent = Agent(
    name='Finance AI Agent',
    model = OpenAIChat(id='gpt-3.5-turbo'),
    tools =[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,
        company_news=True)
    ],
    instructions=['Use tables to display the data'],
    show_tools_calls=True,
    markdown=True
)


app = Playground(agents=[web_search_agent,finance_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)

