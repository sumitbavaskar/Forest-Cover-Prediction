import os
# ✅ Force install dependencies (works even on Streamlit Cloud)
os.system("pip install streamlit joblib pandas numpy scikit-learn requests --quiet")

import streamlit as st
import joblib
import pandas as pd
import requests

# --- Load model from Google Drive ---
# 🔹 Paste ONLY the file ID from your Drive link here
file_id = "1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW"  # 👈 replace with your model file ID
model_url = f"https://drive.google.com/uc?id={file_id}"

@st.cache_resource
def load_model():
    st.info("Downloading model from Google Drive... ⏳")
    response = requests.get(model_url, stream=True)
    model = joblib.load(response.raw)
    return model

# --- App title ---
st.title("🌲 Forest Cover Type Prediction App")

# --- Load model ---
try:
    model = load_model()
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# --- Input Fields ---
st.header("Enter Feature Values")

Elevation = st.number_input("Elevation (in meters)", min_value=0, max_value=5000, value=2000)
Aspect = st.number_input("Aspect (0–360 degrees)", min_value=0, max_value=360, value=180)
Slope = st.number_input("Slope (degrees)", min_value=0, max_value=90, value=10)
Distance = st.number_input("Horizontal Distance To Roadways (in meters)", min_value=0, max_value=10000, value=200)
Soil_Type = st.selectbox("Soil Type", [0, 1, 2, 3, 4, 5, 6, 7])

# --- Prepare input data ---
input_data = pd.DataFrame({
    'Elevation': [Elevation],
    'Aspect': [Aspect],
    'Slope': [Slope],
    'Horizontal_Distance_To_Roadways': [Distance],
    'Soil_Type': [Soil_Type]
})

# --- Predict Button ---
if st.button("Predict Forest Cover Type"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🌳 Predicted Cover Type: {prediction}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
