import streamlit as st
from database.database import save_user_profile

def show_dashboard():
  st.header("Welcome to Your Wellness Dashboard")

  with st.form("user_profile_form"):
    st.subheader("Please fill out your profile")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=10, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    height = st.number_input("Height (cm)", min_value=50, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=300)

    fitness_goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "General Fitness", "Other"])
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])

    dietary_preferences = st.text_input("Dietary Preferences (e.g., Vegan, Keto, Allergies)")
    mental_health_background = st.text_area("Mental Health Background (Optional)")
    daily_schedule = st.text_area("Daily Schedule / Time Availability")
    medical_conditions = st.text_area("Medical Conditions (if any)")

    submitted = st.form_submit_button("Save Profile")

    if submitted:
      profile = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "fitness_goal": fitness_goal,
        "activity_level": activity_level,
        "dietary_preferences": dietary_preferences,
        "mental_health_background": mental_health_background,
        "daily_schedule": daily_schedule,
        "medical_conditions": medical_conditions
      }

      user_id = save_user_profile(profile)
      st.session_state.user_id = user_id
      st.success("Profile saved successfully! You can now access all features.")
