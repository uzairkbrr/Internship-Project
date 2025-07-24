import streamlit as st

def show_exercise_tab():
  st.subheader("Exercise Plan")

  st.text_input("Enter completed workout (e.g., 30 min jog, 15 pushups)")

  if st.button("Log Workout"):
    st.success("Workout logged. Progress tracking coming soon.")
