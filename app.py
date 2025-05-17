import streamlit as st
import pandas as pd

# Load the dataset to extract unique options
@st.cache_data
def load_options():
    df = pd.read_csv("crop_yield.csv")
    crops = sorted(df['Crop'].dropna().unique().tolist())
    seasons = sorted([s.strip() for s in df['Season'].dropna().unique()])
    states = sorted(df['State'].dropna().unique().tolist())
    return crops, seasons, states

# Load dropdown options from dataset
crops, seasons, states = load_options()

# App UI
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")
st.title("🌾 Crop Yield Prediction App")

with st.form("yield_form"):
    st.subheader("📋 Enter Input Parameters")

    col1, col2 = st.columns(2)

    with col1:
        crop = st.selectbox("Crop:", crops)
        crop_year = st.number_input("Crop Year:", min_value=2000, max_value=2100, value=2025)
        season = st.selectbox("Season:", seasons)
        state = st.selectbox("State:", states)
        area = st.number_input("Area (ha):", min_value=0.0, step=0.1)

    with col2:
        production = st.number_input("Production (tons):", min_value=0.0, step=0.1)
        rainfall = st.number_input("Annual Rainfall (mm):", min_value=0.0, step=0.1)
        fertilizer = st.number_input("Fertilizer Used (kg):", min_value=0.0, step=0.1)
        pesticide = st.number_input("Pesticide Used (kg):", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🔍 Predict Yield")

# Dummy Prediction Logic
if submitted:
    if area == 0:
        st.error("Area must be greater than 0.")
    else:
        predicted_yield = (
            (production / area)
            + (rainfall * 0.01)
            + (fertilizer * 0.2)
            + (pesticide * 0.1)
            + (crop_year % 100) * 0.4
        )
        st.success(f"🌱 Predicted Yield: {predicted_yield:.2f} tons/ha")
