from fastapi import FastAPI
from app.models.schema import QueryRequest
from app.agents.multi_agent import multi_agent_executor

app = FastAPI()

@app.post("/ask")
async def ask_question(request: QueryRequest):
    response = multi_agent_executor.chat(request.query)
    return {"response": str(response)}
