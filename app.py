# app_auto_mpg.py

import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Load the trained model
# -----------------------------
@st.cache_resource
def load_model():
    # 👉 Change the file name here if needed
    with open("model_before.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -----------------------------
# Streamlit page settings
# -----------------------------
st.set_page_config(
    page_title="Auto MPG Predictor",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Auto MPG Prediction App")
st.write(
    "Enter the car features below to predict the fuel efficiency in **mpg** "
    "using your trained machine learning model."
)

# -----------------------------
# Inputs from user
# -----------------------------
st.subheader("Input Features")

col1, col2 = st.columns(2)

with col1:
    horsepower = st.number_input(
        "Horsepower",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=1.0
    )

with col2:
    weight = st.number_input(
        "Weight (in lbs)",
        min_value=0.0,
        max_value=10000.0,
        value=2500.0,
        step=10.0
    )

acceleration = st.number_input(
    "Acceleration (0–60 mph time or similar)",
    min_value=0.0,
    max_value=30.0,
    value=15.0,
    step=0.1
)

# -----------------------------
# Predict button
# -----------------------------
if st.button("Predict MPG"):
    # Prepare data for model: shape (1, 3)
    input_data = np.array([[horsepower, weight, acceleration]])

    try:
        predicted_mpg = model.predict(input_data)[0]
        st.success(f"🔮 Predicted MPG: **{predicted_mpg:.2f}**")
    except Exception as e:
        st.error(f"Error while making prediction: {e}")
        st.info(
            "Make sure the model expects features in this order: "
            "`['horsepower', 'weight', 'acceleration']`."
        )

st.caption("App created using your saved Auto MPG model file.")
