import streamlit as st
from auth.auth import register_user, authenticate_user

def show_authentication():
  st.title("Welcome to Wellness Assistant")

  if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_id = None

  mode = st.radio("Choose action:", ["Login", "Sign Up"])

  if mode == "Sign Up":
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
      if password != confirm:
        st.error("Passwords do not match.")
      else:
        success, msg = register_user(username, email, password)
        if success:
          st.success(msg)
        else:
          st.error(msg)

  else:  # Login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
      valid, user_id = authenticate_user(username, password)
      if valid:
        st.session_state.authenticated = True
        st.session_state.user_id = user_id
        st.success("Login successful!")
        st.experimental_rerun()
      else:
        st.error("Invalid username or password.")
