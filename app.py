import os
os.system("pip install joblib pandas numpy scikit-learn requests --quiet")

import streamlit as st
import joblib
import pandas as pd
import requests
import numpy as np


# --- Load model from Google Drive ---
file_id = "1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW"  # <-- apna Drive file ID yahan daal
model_url = "https://drive.google.com/file/d/1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW/view?usp=sharing{1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW}"

@st.cache_resource
def load_model():
    response = requests.get(model_url, stream=True)
    model = joblib.load(response.raw)
    return model

model = load_model()

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
    st.success(f"Predicted Cover Type: {pred}")
