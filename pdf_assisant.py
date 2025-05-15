import typer
from typing import Optional,List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
db_url='postgresql+psycopg://ai:ai@localhost:5532/ai'


knowledgebase= PDFUrlKnowledgeBase(
    urls=['https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf'],
    vector_db= PgVector2(collection='recipes',db_url=db_url)
)


knowledgebase.load()

storage = PgAssistantStorage(table_name ='pdf_assistant',db_url=db_url)