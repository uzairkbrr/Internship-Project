import streamlit as st
from utils.llm_wrapper import chat_with_llm
from utils.intent_classifier import is_mental_health_related
from database.database import get_user_profile, save_memory_entry

def show_mental_health_tab():
  st.header("Mental Health Companion")

  if "user_id" not in st.session_state:
    st.warning("Please complete your user profile in the Dashboard first.")
    return

  user_id = st.session_state.user_id
  profile = get_user_profile(user_id)

  st.checkbox("Memory Mode", key="memory_mode")
  user_input = st.text_area("How are you feeling today?", key="mental_input")

  if st.button("Send"):
    if not is_mental_health_related(user_input):
      st.error("This message does not seem related to mental health.")
      return

    system_msg = (
      f"You are a friendly mental health companion. "
      f"The user is {profile[1]}, a {profile[3]} aged {profile[2]}, "
      f"with fitness goal: {profile[5]}. "
      f"Offer emotional support based on their mental health background: {profile[8]}"
    )

    messages = [
      {"role": "system", "content": system_msg},
      {"role": "user", "content": user_input}
    ]

    llm_response = chat_with_llm(messages)
    st.write("Assistant:", llm_response)

    if st.session_state.memory_mode:
      save_memory_entry(user_id, user_input, llm_response, emotion=None)  # Emotion can be added later
