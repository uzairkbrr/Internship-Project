import streamlit as st
from database.database import get_user_profile

def show_diet_tab():
  st.header("Diet Tracker")

  if "user_id" not in st.session_state:
    st.warning("Please complete your user profile in the Dashboard first.")
    return

  user_id = st.session_state.user_id
  profile = get_user_profile(user_id)

  st.write("Your dietary preference:", profile[7])
  st.write("Fitness goal:", profile[5])

  # Additional functionality for meal input, image upload, etc. will go here
