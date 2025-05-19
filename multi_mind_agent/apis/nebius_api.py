"""
nebius_api.py

This module handles both code/text and image generation by connecting to
Nebius AI Studio using its OpenAI-compatible client. It is responsible for
abstracting the underlying model calls, managing API authentication, routing
requests based on task type, decoding image output from base64, and handling
errors gracefully.

The system uses two separate models on Nebius:
- A large language model (Meta-LLaMA 3.1) for code/text generation
- A diffusion-based model (Flux) for high-quality image synthesis

Image output is saved locally and displayed using PIL.
"""

import os
import base64
from PIL import Image
from openai import OpenAI

# Load the IAM token required to authenticate with Nebius AI Studio.
# This token is stored in a separate file to keep credentials secure.
with open("keys/nebius_api_key.txt", "r") as f:
    os.environ["NEBIUS_API_KEY"] = f.read().strip()

# Initialize a client for Nebius using OpenAI's SDK pattern.
# The base_url is customized to target Nebius's version of the OpenAI API.
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ["NEBIUS_API_KEY"]
)

# Model identifiers configured for use in this project.
# These IDs are provided by Nebius AI Studio and should be updated
# based on available model access.
TEXT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct"
IMAGE_MODEL = "black-forest-labs/flux-dev"

def generate_with_nebius(prompt, task_type):
    """
    Main dispatcher function that sends prompts to the appropriate Nebius model.

    Args:
        prompt (str): The user input to process (text/code/image request).
        task_type (str): Type of the task, either 'code' or 'image'.

    Returns:
        str: The generated response (text or image display status message).
    """

    if task_type == "code":
        # --------------------------------------------------------------
        # This block handles code generation using Nebius's LLM.
        # The prompt is wrapped inside a chat-like format expected by
        # OpenAI-compatible chat completion models.
        # --------------------------------------------------------------
        try:
            response = client.chat.completions.create(
                model=TEXT_MODEL,
                messages=[
                    {"role": "system", "content": "You are a smart assistant that writes code."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"❌ Error generating code via Nebius: {str(e)}"

    elif task_type == "image":
        # --------------------------------------------------------------
        # This block handles image generation using Nebius's diffusion model.
        # The prompt is sent along with extra parameters such as image size,
        # seed, and step count. The response is base64-encoded, which we decode,
        # save as a .png image, and display using the PIL library.
        # --------------------------------------------------------------
        try:
            response = client.images.generate(
                model=IMAGE_MODEL,
                response_format="b64_json",
                prompt=prompt,
                extra_body={
                    "response_extension": "png",
                    "width": 1024,
                    "height": 1024,
                    "num_inference_steps": 28,
                    "negative_prompt": "",
                    "seed": -1
                }
            )

            # Extract the base64-encoded image string from the API response.
            b64_image = response.data[0].b64_json
            image_data = base64.b64decode(b64_image)

            # Save the decoded image to disk.
            temp_path = "output_generated_image.png"
            with open(temp_path, "wb") as f:
                f.write(image_data)

            # Load and display the image using PIL.
            image = Image.open(temp_path)
            image.show()

            return "🖼 Image generated and displayed successfully."

        except Exception as e:
            return f"❌ Error generating image via Nebius: {str(e)}"

    else:
        # --------------------------------------------------------------
        # If the task type provided is neither 'code' nor 'image',
        # the system cannot route the request and returns a failure.
        # --------------------------------------------------------------
        return "❌ Unknown task type requested for Nebius."
