from agent_logic import run_agent

def main():
    print("🧠 MultiMind Agent is ready!")
    print("Type something (or type 'exit' to quit):")

    while True:
        user_input = input("\nYou: ")


        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye! MultiMind Agent shutting down.")
            break
        response = run_agent(user_input)

        print("Agent:", response)


if __name__ == "__main__":
    main()
