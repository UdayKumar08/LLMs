🧠 MultiMind Agent

MultiMind Agent is a command-line-based intelligent assistant system designed to demonstrate how different AI capabilities (language understanding, code generation, and image generation)
can be orchestrated together using modular design and dynamic task routing. This system accepts natural language input from a user, identifies the user's intent behind the message, and selects
the most appropriate model or API to fulfill that intent. Its main strength lies in combining both OpenAI’s GPT models (for general chat and text tasks) and Nebius AI Studio’s multimodal models
(for generating code and images) — with a simple but powerful decision engine at the core.

📌 Problem the Project Solves

Instead of building three different apps for text Q&A, coding, and image generation, this single intelligent agent understands your intent and picks the right backend automatically — saving time 
and enabling unified interaction with multiple LLMs.
![image](https://github.com/user-attachments/assets/c7d3d65d-84d0-49cc-bb4c-d7ec6e041fb6)

🧠 Functional Flow (Step-by-Step Understanding)

User starts the program using main.py. This opens a continuous input loop through the command-line interface.

User types a prompt, like:

"What is quantum computing?"

"Write a Python function for factorial."

"Generate an image of a galaxy shaped like a butterfly."

The message is passed to the agent_logic module, which does keyword-based analysis to detect intent:

If it contains words like “image”, “draw”, “picture” → it classifies as image

If it includes “code”, “script”, “function”, “program” → it classifies as code

Otherwise → it's text

Based on the intent, the agent routes the prompt:

If text, it calls openai_chat.py using OpenAI GPT-3.5-Turbo

If code or image, it calls nebius_api.py using Nebius Meta-LLaMA or Diffusion model

The result is returned and printed directly. If it is an image, it’s decoded from base64 and shown in a pop-up.

🧰 Core Features

Smart task detection from user prompts

Modular routing engine for scalable model integration

Uses OpenAI ChatGPT (gpt-3.5-turbo) for general conversations

Uses Nebius Meta-LLaMA for code generation

Uses Nebius diffusion model to create realistic images

Images automatically displayed and saved as PNG

🧱 Project Folder Structure

multi_mind_agent/
├── main.py                 ← CLI interface, entry point
├── agent_logic.py          ← Task routing and classification
├── apis/
│   ├── openai_chat.py      ← OpenAI GPT handler
│   └── nebius_api.py       ← Nebius code + image generator
├── keys/
│   ├── openai_api_key.txt
│   └── nebius_api_key.txt

🔧 Installation & Setup

Clone or download the project folder.

Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

Install dependencies:

pip install openai Pillow

Add API Keys:

Paste your OpenAI API key inside: keys/openai_api_key.txt

Paste your Nebius IAM token inside: keys/nebius_api_key.txt

Run the main agent:

python main.py

✨ Supported Prompts & Examples

Text / Chat:

You: What is the capital of France?
→ Agent: The capital of France is Paris.

Code Generation:

You: Write a Python program to check if a number is prime.
→ Agent: (returns working code using Nebius LLaMA)

Image Generation:

You: Draw a robot holding a sunflower in a field.
→ Agent: (shows generated image using Nebius image model)

🔍 How Internal Logic Works

Steps for Module Description

1 main.py
Accepts user input through CLI

2 agent_logic.py
Classifies prompt using keywords

3 openai_chat.py
Called if it's a general question (text)

4 nebius_api.py
Called if it’s code or image

5 PIL
Used to display generated image from base64

🧠 Models Used
gpt-3.5-turbo from OpenAI (via openai.ChatCompletion)
meta-llama/Meta-Llama-3.1-70B-Instruct from Nebius (code LLM)
black-forest-labs/flux-dev from Nebius (diffusion image generator)

📷 Architecture Diagram

You can view the complete system architecture here:

🔮 Future Enhancements

Add voice input using Whisper

Integrate memory/context with SQLite

Connect to RAG via LangChain for document awareness

Add web UI using Streamlit or Gradio

Track usage logs for analytics

🙌 Acknowledgements

This project was designed to explore how multi-agent workflows can be handled by routing one input to many models based on context. It combines natural language processing, code generation,
and computer vision using publicly available models in a practical, user-friendly format.

It’s built in a modular, readable structure so future developers can swap models or backends easily.

Created with curiosity and LLMs.

