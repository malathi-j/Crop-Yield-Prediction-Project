import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and encoders
try:
    model = joblib.load("crop_yield_model.pkl")
    encoders = joblib.load("label_encoders.pkl")
except FileNotFoundError as e:
    st.error("❌ Model or encoders not found. Please ensure 'crop_yield_model.pkl' and 'label_encoders.pkl' are in the same directory.")
    st.stop()

st.title("🌾 Crop Yield Prediction App")
st.write("This app predicts crop yield (in tons/hectare) based on environmental and agricultural parameters.")

# Input form
with st.form("yield_form"):
    crop = st.text_input("Crop (e.g., Rice, Maize)")
    crop_year = st.number_input("Crop Year", min_value=1990, max_value=2100, value=2024)
    season = st.text_input("Season (e.g., Kharif, Rabi, Whole Year)")
    state = st.text_input("State (e.g., Karnataka, Punjab)")
    area = st.number_input("Area (hectares)", min_value=0.0, value=1.0)
    production = st.number_input("Production (tons)", min_value=0.0, value=1.0)
    rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0, value=800.0)
    fertilizer = st.number_input("Fertilizer Used (kg/ha)", min_value=0.0, value=50.0)
    pesticide = st.number_input("Pesticide Used (kg/ha)", min_value=0.0, value=5.0)

    submit = st.form_submit_button("Predict Yield")

if submit:
    try:
        # Encode categorical inputs
        crop_encoded = encoders['Crop'].transform([crop])[0]
        season_encoded = encoders['Season'].transform([season])[0]
        state_encoded = encoders['State'].transform([state])[0]

        # Build input vector
        input_data = pd.DataFrame([[
            crop_encoded,
            crop_year,
            season_encoded,
            state_encoded,
            area,
            production,
            rainfall,
            fertilizer,
            pesticide
        ]], columns=['Crop', 'Crop_Year', 'Season', 'State', 'Area', 'Production',
                     'Annual_Rainfall', 'Fertilizer', 'Pesticide'])

        # Predict
        prediction = model.predict(input_data)[0]
        st.success(f"🌾 Estimated Crop Yield: **{prediction:.2f} tons/hectare**")

    except ValueError as ve:
        st.error(f"❌ Value Error: {ve}")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")
