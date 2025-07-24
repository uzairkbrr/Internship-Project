import streamlit as st
from frontend.auth_ui import show_authentication
from frontend.dashboard import show_dashboard
from frontend.mental_health import show_mental_health_tab
from frontend.diet import show_diet_tab
from frontend.exercise import show_exercise_tab

from dotenv import load_dotenv
load_dotenv()

from database.database import init_db
init_db()

st.set_page_config(page_title="Wellness Assistant", layout="wide")

if "authenticated" not in st.session_state or not st.session_state.authenticated:
  show_authentication()
else:
  st.sidebar.title("Navigation")
  page = st.sidebar.radio("Go to", ["Dashboard", "Mental Health", "Diet Tracker", "Exercise Plan"])
  st.title("Agentic Wellness Assistant")

  if page == "Dashboard":
    show_dashboard()
  elif page == "Mental Health":
    show_mental_health_tab()
  elif page == "Diet Tracker":
    show_diet_tab()
  elif page == "Exercise Plan":
    show_exercise_tab()
