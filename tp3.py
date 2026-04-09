from app.agent import create_agent
from app.middleware import guardrails, human_in_loop

agent = create_agent()

while True:
    query = input("You: ")

    query = guardrails(query)

    response = agent.run(query)

    final = human_in_loop(response)

    print("Final:", final)