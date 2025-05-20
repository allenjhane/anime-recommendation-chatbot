# chatbot.py

import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# -----------------------------------------------------------------------------
# 1) Auto-load .env (finds it in your project root or parent dirs)
# -----------------------------------------------------------------------------
load_dotenv(find_dotenv())

# -----------------------------------------------------------------------------
# 2) Read the key and validate
# -----------------------------------------------------------------------------
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not set in environment. "
        "Make sure you have a .env file with OPENAI_API_KEY=sk-... or "
        "that you exported it in your shell."
    )

# -----------------------------------------------------------------------------
# 3) Instantiate the OpenAI client
# -----------------------------------------------------------------------------
client = OpenAI(api_key=api_key)

# -----------------------------------------------------------------------------
# 4) Chat function
# -----------------------------------------------------------------------------
def chat_with_gpt(user_message, recommendations=None):
    """
    Sends a prompt to OpenAI’s chat endpoint and returns the reply.
    `recommendations` can be a list of anime titles to include.
    """
    system_prompt = (
        "You are an anime-loving assistant. "
        "Suggest up to 5 similar anime based on the user's input, "
        "giving a one-sentence explanation for each."
    )
    user_content = (
        f"The user said: \"{user_message}\"\n"
        f"Recommendations to highlight: {recommendations}"
    )

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_content},
        ],
        temperature=0.7,
        # max_tokens=200,
    )
    return response.choices[0].message.content.strip()
