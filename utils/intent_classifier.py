# utils/intent_classifier.py

from utils.llm_wrapper import chat_with_llm

def is_mental_health_related(user_input):
  prompt = [
    {"role": "system", "content": "You are a classifier that determines whether a user's message is related to mental health, journaling, or emotional support. Only respond with 'Yes' or 'No'."},
    {"role": "user", "content": f"Is this related to mental health or journaling? '{user_input}'"}
  ]

  response = chat_with_llm(prompt).strip().lower()
  return response.startswith("yes")
