%%writefile app.py
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')

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
