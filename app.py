import os
# ✅ Force install dependencies (guaranteed fix)
os.system("pip install streamlit joblib pandas numpy scikit-learn requests --quiet")

import streamlit as st
import joblib
import pandas as pd
import requests
import io

# --- Load model from Google Drive ---
# Replace this with your own Google Drive File ID
file_id = "1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW"  # 👈 apna file ID yahan daal
model_url = f"https://drive.google.com/uc?id={file_id}"

@st.cache_resource
def load_model():
    response = requests.get(model_url, stream=True)
    model = joblib.load(io.BytesIO(response.content))
    return model

st.write("Loading model... please wait ⏳")
model = load_model()
st.success("✅ Model loaded successfully!")

# --- Streamlit App UI ---
st.title("🌲 Forest Cover Type Prediction App")

Elevation = st.number_input("Elevation", 0, 5000, 2000)
Aspect = st.number_input("Aspect", 0, 360, 180)
Slope = st.number_input("Slope", 0, 90, 10)
Distance = st.number_input("Horizontal_Distance_To_Roadways", 0, 10000, 200)
Soil_Type = st.selectbox("Soil Type", [0,1,2,3,4,5,6,7])

data = pd.DataFrame({
    'Elevation': [Elevation],
    'Aspect': [Aspect],
    'Slope': [Slope],
    'Horizontal_Distance_To_Roadways': [Distance],
    'Soil_Type': [Soil_Type]
})

if st.button("Predict"):
    pred = model.predict(data)[0]
    st.success(f"🌿 Predicted Cover Type: {pred}")
