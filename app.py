from agent import get_agent

agent = get_agent()

print("Phidata LLM Chat (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break
    response = agent.run(user_input)
    print(f"Agent: {response.content}\n")
