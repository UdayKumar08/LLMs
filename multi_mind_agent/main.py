"""
main.py

This is the entry point of the MultiMind Agent system. It provides a
simple command-line interface (CLI) for the user to interact with the
agent. The core purpose of this script is to continuously accept user
input, pass it through the agent logic for processing, and display
the result — whether it's a conversational response, code generation,
or an image request.

The interaction loop runs until the user explicitly exits the session.
"""

from agent_logic import run_agent

def main():
    """
    Launches the CLI interface and runs an infinite loop to process input
    and deliver output based on the type of task detected and executed.
    """
    print("🧠 MultiMind Agent is ready!")
    print("Type something (or type 'exit' to quit):")

    while True:
        # --------------------------------------------------------------
        # Capture user input from the terminal. This is the primary method
        # of sending prompts into the system. Input can be conversational,
        # code-related, or image requests.
        # --------------------------------------------------------------
        user_input = input("\nYou: ")

        # --------------------------------------------------------------
        # Check for session termination commands. If the user types 'exit'
        # or 'quit' (case-insensitive), the loop breaks and the program ends.
        # --------------------------------------------------------------
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye! MultiMind Agent shutting down.")
            break

        # --------------------------------------------------------------
        # Route the input to the agent’s brain (`run_agent`), which internally
        # decides whether to use ChatGPT, Nebius LLaMA, or the Nebius image model.
        # --------------------------------------------------------------
        response = run_agent(user_input)

        # --------------------------------------------------------------
        # Display the agent's output. For text or code, this prints directly.
        # For image prompts, image display is handled separately via PIL.
        # --------------------------------------------------------------
        print("Agent:", response)

# ----------------------------------------------------------------------
# This check ensures that the CLI only runs when this script is executed
# directly, not when it is imported as a module in another program.
# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
