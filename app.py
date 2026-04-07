import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Customer Churn Prediction App")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0.0, 200.0, 70.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# Create input dataframe
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "Contract": [contract]
})

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("High chance of churn")
    else:
        st.success("Low chance of churn")

    st.write(f"Churn probability: {probability:.2%}")