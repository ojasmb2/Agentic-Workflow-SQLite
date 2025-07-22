from llama_index.agent import MultiAgentExecutor
from app.agents.base_agent import sql_agent

# You could define other specialized agents similarly if needed
multi_agent_executor = MultiAgentExecutor.from_agents(
    agents=[sql_agent],
    llm=sql_agent.llm,
    verbose=True
)