import streamlit as st
import base64

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Change this path if your app.py is not in same folder as the image
image_path = r"C:\Users\malat\Downloads\bg.jpg"
image_base64 = get_base64_of_bin_file(image_path)

page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] > .main {{
  background-image: url("data:image/jpg;base64,{image_base64}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
}}

[data-testid="stAppViewContainer"] {{
  background: transparent;
}}

[data-testid="stHeader"], [data-testid="stToolbar"], footer {{
  background: rgba(255, 255, 255, 0.85);
  border-radius: 10px;
  padding: 8px;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🌾 Crop Yield Prediction")

# Your form and other code here — same as before
crops = [
    'Wheat', 'Rice', 'Maize', 'Barley', 'Millet', 'Sorghum', 'Soybean', 'Cotton', 'Sugarcane',
    'Groundnut', 'Mustard', 'Sunflower', 'Tea', 'Coffee', 'Potato', 'Tomato', 'Onion', 'Chili',
    'Banana', 'Mango', 'Apple'
]

seasons = [
    'Summer', 'Winter', 'Monsoon', 'Autumn', 'Spring', 'Rabi', 'Kharif', 'Zaid'
]

states = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
    'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
    'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
    'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
    'Uttarakhand', 'West Bengal', 'Delhi'
]

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

if submitted:
    if area == 0:
        st.error("Area cannot be zero to calculate yield.")
    else:
        predicted_yield = (
            (production / area)
            + (rainfall * 0.01)
            + (fertilizer * 0.2)
            + (pesticide * 0.1)
            + (crop_year % 100) * 0.4
        )
        st.success(f"🌱 Predicted Yield: {predicted_yield:.2f} tons/ha")





