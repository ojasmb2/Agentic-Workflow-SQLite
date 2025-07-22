from sqlalchemy import create_engine
from llama_index.indices.struct_store.sql_query import SQLDatabase

engine = create_engine("sqlite:///database/sakila.db")
sql_database = SQLDatabase(engine)