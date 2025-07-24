import streamlit as st
from database.database import get_user_profile

def show_exercise_tab():
  st.header("Exercise Planner")

  if "user_id" not in st.session_state:
    st.warning("Please complete your user profile in the Dashboard first.")
    return

  user_id = st.session_state.user_id
  profile = get_user_profile(user_id)

  st.write("Fitness Goal:", profile[5])
  st.write("Activity Level:", profile[6])

  # Add logic for generating or logging workouts
