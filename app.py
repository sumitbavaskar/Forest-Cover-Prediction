import os
# Force install dependencies
os.system("pip install streamlit joblib pandas numpy scikit-learn requests --quiet")
import streamlit as st
import joblib
import pandas as pd
import requests
import io

# Load model from Google Drive
file_id = "1tWd2v7Fzbv44tPLw4z2OOYxW6dfcmScW"
model_url = f"https://drive.google.com/uc?id={file_id}"

@st.cache_resource
def load_model():
    response = requests.get(model_url, stream=True)
    model = joblib.load(io.BytesIO(response.content))
    return model

st.write("Loading model... please wait ⏳")
model = load_model()
st.success("✅ Model loaded successfully!")

# Streamlit App UI
st.title("🌲 Forest Cover Type Prediction App")

st.write("### Input Parameters:")
Elev = st.slider("Elevation", 1000, 4000, 2000)
Asp = st.slider("Aspect", 0, 360, 180)
Slp = st.slider("Slope", 0, 90, 10)
Hd_Road = st.slider("Horz Distance to Roadways", 0, 10000, 200)
Hd_Fire = st.slider("Horz Distance to Fire Points", 0, 40000, 1000)
Hd_Hydro = st.slider("Horz Distance to Hydrology", 0, 10000, 200)
Vert_Hydro = st.slider("Vertical Distance to Hydrology", -150, 600, 0)
Hydrology = st.selectbox("Hydrology Fire", [0, 1, 2, 3, 4])
Wilderness = st.selectbox("Wilderness Type", [0, 1, 2, 3])
Soil_Type = st.selectbox("Soil Type", list(range(40)))

if st.button("Predict", key="predict_btn"):
    try:
        # Create feature vector with all required features
        features = pd.DataFrame([{
            'Elevation': Elev,
            'Aspect': Asp,
            'Slope': Slp,
            'Horizontal_Distance_To_Roadways': Hd_Road,
            'Horizontal_Distance_To_Fire_Points': Hd_Fire,
            'Horizontal_Distance_To_Hydrology': Hd_Hydro,
            'Vertical_Distance_To_Hydrology': Vert_Hydro,
            'Hydrology_Fire': Hydrology,
            'Wilderness_Type': Wilderness,
            'Soil_Type': Soil_Type
        }])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Display result
        st.success(f"🌿 **Predicted Forest Cover Type: {int(prediction)}**")
        
        cover_types = {
            1: "Spruce/Fir",
            2: "Lodgepole Pine",
            3: "Ponderosa Pine",
            4: "Cottonwood/Willow",
            5: "Aspen",
            6: "Douglas-fir",
            7: "Krummholz"
        }
        
        cover_name = cover_types.get(int(prediction), f"Type {int(prediction)}")
        st.info(f"📍 Forest Cover: **{cover_name}**")
        
    except Exception as e:
        st.error(f"❌ Prediction Error: {str(e)[:100]}")
        st.info("Please check your input values and try again.")
