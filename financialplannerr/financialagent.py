from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

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


multi_ai_agent = Agent(
    team = [web_search_agent,finance_agent],
    instructions = ['Always include sources','Use table to display the data'],
    show_tool_calls= True,
    markdown=True
)


multi_ai_agent.print_response('Summarize Analyst recommendations and share the latest news for NVDA',stream=True)





