"""
openai_chat.py

This module provides a wrapper function for interacting with OpenAI's ChatGPT API
using the modern OpenAI SDK (v1.x+). It is used for handling general-purpose
text-based queries such as natural language questions, explanations, and conversation.

This file handles:
- Loading API credentials securely
- Initializing the OpenAI client
- Sending user prompts as chat messages
- Extracting and returning model responses
"""

import os
from openai import OpenAI

# ----------------------------------------------------------------------
# Load OpenAI API key securely from a local text file and inject it
# into the environment variables. This key is required to authenticate
# every request sent to OpenAI’s cloud-based API services.
# ----------------------------------------------------------------------
with open("keys/openai_api_key.txt", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()

# ----------------------------------------------------------------------
# Create a new OpenAI client instance using the secure API key.
# This client acts as the interface between our application and OpenAI’s
# chat completion endpoint. No base_url is needed because it defaults
# to OpenAI's public endpoint.
# ----------------------------------------------------------------------
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

def ask_chatgpt(user_prompt):
    """
    Sends a chat-style prompt to OpenAI’s GPT model and returns the response.

    Args:
        user_prompt (str): The user's input query or instruction.

    Returns:
        str: The natural language reply from ChatGPT, or an error message.
    """
    try:
        # --------------------------------------------------------------
        # Compose a message in chat format, specifying both a system prompt
        # (which sets the assistant's role) and the user prompt.
        # This is the preferred input format for chat-based GPT models.
        # --------------------------------------------------------------
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )

        # --------------------------------------------------------------
        # Extract the assistant’s textual response from the returned object.
        # The response typically contains an array of message choices; we
        # return the first one after stripping whitespace.
        # --------------------------------------------------------------
        return response.choices[0].message.content.strip()

    except Exception as e:
        # --------------------------------------------------------------
        # If any error occurs during the API call (e.g., network, auth, limits),
        # this block ensures we return a meaningful message without crashing.
        # --------------------------------------------------------------
        return f"⚠️ Error using ChatGPT: {str(e)}"
