from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from app.tools import tools
from app.memory import memory

def create_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

    return agent