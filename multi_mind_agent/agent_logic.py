
from apis.openai_chat import ask_chatgpt
from apis.nebius_api import generate_with_nebius

def run_agent(user_input):

    input_lower = user_input.lower()


    if any(keyword in input_lower for keyword in ["image", "draw", "picture", "visual"]):
        task_type = "image"
    elif any(keyword in input_lower for keyword in ["code", "function", "script", "program"]):
        task_type = "code"
    else:
        task_type = "text"

    if task_type in ["image", "code"]:
        response = generate_with_nebius(user_input, task_type)
    else:
        response = ask_chatgpt(user_input)

    return response