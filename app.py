import streamlit as st

# Set page title
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction")

# Sample dropdown data
crops = ['Wheat', 'Rice', 'Maize', 'Barley']
seasons = ['Summer', 'Winter', 'Monsoon']
states = ['Karnataka', 'Maharashtra', 'Punjab', 'Tamil Nadu']

# Input form
with st.form("crop_form"):
    col1, col2 = st.columns(2)
    with col1:
        crop = st.selectbox("Select Crop:", crops)
        crop_year = st.number_input("Enter Crop Year:", min_value=1900, max_value=2100, value=2025)
        season = st.selectbox("Select Season:", seasons)
        state = st.selectbox("Select State:", states)
        area = st.number_input("Enter Area (ha):", min_value=0.0, step=0.1)
    with col2:
        production = st.number_input("Enter Production (tons):", min_value=0.0, step=0.1)
        rainfall = st.number_input("Enter Annual Rainfall (mm):", min_value=0.0, step=0.1)
        fertilizer = st.number_input("Enter Fertilizer Used (kg):", min_value=0.0, step=0.1)
        pesticide = st.number_input("Enter Pesticide Used (kg):", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    if area == 0:
        st.error("Area cannot be zero to calculate yield.")
    else:
        # Dummy prediction formula (replace with actual model prediction)
        predicted_yield = (
            (production / area)
            + (rainfall * 0.01)
            + (fertilizer * 0.2)
            + (pesticide * 0.1)
            + (crop_year % 100) * 0.4
        )

        st.success(f"🌱 Predicted Yield: {predicted_yield:.2f} tons/ha")
