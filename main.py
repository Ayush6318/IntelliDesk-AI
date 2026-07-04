from agent.agent import agent

print("=" * 50)
print("🤖 Welcome to IntelliDesk AI")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }
    )

    print("\nAI:", response["messages"][-1].content)