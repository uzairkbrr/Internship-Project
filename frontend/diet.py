import streamlit as st

def show_diet_tab():
  st.subheader("Diet Tracker")

  st.text_input("Enter your meal (e.g., 2 eggs and toast)")

  uploaded_img = st.file_uploader("Upload Meal Photo", type=["jpg", "jpeg", "png"])

  if st.button("Analyze"):
    st.success("Diet analysis will be shown here.")
