# utils/llm_wrapper.py

import requests
import os

# Load API key from environment variable
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
print(TOGETHER_API_KEY)
BASE_URL = "https://api.together.xyz/v1/chat/completions"

model = "meta-llama/Llama-3-8b-chat-hf"

def chat_with_llm(messages, model=model, temperature=0.7, max_tokens=1024):
    """
    Send a list of messages to Together.ai and return the assistant's response.

    Parameters:
    - messages: list of dicts like [{role: "user", content: "Hi"}, {role: "assistant", content: "..."}]
    - model: Model name to use (default LLaMa 3.1 8b)
    - temperature: Response randomness
    - max_tokens: Max tokens to generate

    Returns:
    - LLM's response (string)
    """

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']

    except Exception as e:
        print("Error communicating with Together.ai:", e)
        return "⚠️ Sorry, there was a problem communicating with the AI."
