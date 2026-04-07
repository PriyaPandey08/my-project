import streamlit as st
import pandas as pd
import pickle

st.title("Customer Churn Prediction App")

# Sample inputs
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.slider("Monthly Charges", 0, 200)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# Simple encoding (basic for now)
contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

# Dummy model logic (we will improve later)
if st.button("Predict"):
    if tenure < 12 and contract == "Month-to-month":
        st.error("High chance of churn ❌")
    else:
        st.success("Low chance of churn ✅")