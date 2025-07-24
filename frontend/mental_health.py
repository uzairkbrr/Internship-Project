import streamlit as st

def show_mental_health_tab():
  st.subheader("Mental Health Support")

  memory_mode = st.toggle("Enable Memory Mode")
  user_input = st.text_area("How are you feeling today?", placeholder="Start journaling or ask for support...")

  if st.button("Send"):
    st.success(f"Sent message with memory = {memory_mode}")
    # Placeholder for integration with LLM
