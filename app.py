import streamlit as st

# 1. Set page config as the very first Streamlit command
st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# 2. Inject CSS for background image
page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Ffsii.in%2Fmonoculture-farming%2F&psig=AOvVaw3kn1RHoNiocjZHHXgZm8aH&ust=1747588838129000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKi4o_WBq40DFQAAAAAdAAAAABAE");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
.stApp {
    background: transparent;
}
footer, header, .css-1v3fvcr, .css-1d391kg {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    padding: 10px;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# 3. Rest of your UI code
st.title("🌾 Crop Yield Prediction")

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


