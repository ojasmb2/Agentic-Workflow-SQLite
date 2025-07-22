from llama_index.llms import OpenAI
from llama_index.agent import SQLAgent
from app.db.connection import sql_database

llm = Ollama(
    model="llama3",  # or use "llama3:instruct" if needed
    request_timeout=60.0
)

sql_agent = SQLAgent(
    sql_database=sql_database,
    llm=llm,
    verbose=True
)
