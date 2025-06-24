
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('youngsters_heart_risk_model.pkl')

st.title("🫀 Heart Attack Risk Predictor for Youngsters")

age = st.number_input("Age", 15, 45)
bp = st.number_input("Blood Pressure (mm Hg)")
chol = st.number_input("Cholesterol Level (mg/dL)")
# Add more inputs as per your dataset

if st.button("Predict"):
    input_data = [[age, bp, chol]]  # Ensure this matches the model input order
    prediction = model.predict(input_data)
    result = "High Risk 💔" if prediction[0] == 1 else "Low Risk 💖"
    st.success(f"Prediction: {result}")
