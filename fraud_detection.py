import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

st.title("💳 Fraud Detection App")

st.write("Enter the transaction details to check if it is fraudulent.")

st.divider()

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT","TRANSFER","CASH_OUT","DEBIT","CASH_IN"]
)

amount = st.number_input("Transaction Amount", min_value=0.0, value=100.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=9200.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=800.0)

if st.button("Predict Fraud"):

    # Base features
    df = pd.DataFrame({
        "amount":[amount],
        "oldbalanceOrg":[oldbalanceOrg],
        "newbalanceOrig":[newbalanceOrig],
        "oldbalanceDest":[oldbalanceDest],
        "newbalanceDest":[newbalanceDest]
    })

    # Feature engineering
    df["balanceDiffOrig"] = df["oldbalanceOrg"] - df["newbalanceOrig"]
    df["balanceDiffDest"] = df["oldbalanceDest"] - df["newbalanceDest"]

    # One-hot encoding for transaction type
    df["type_CASH_OUT"] = 1 if transaction_type == "CASH_OUT" else 0
    df["type_DEBIT"] = 1 if transaction_type == "DEBIT" else 0
    df["type_PAYMENT"] = 1 if transaction_type == "PAYMENT" else 0
    df["type_TRANSFER"] = 1 if transaction_type == "TRANSFER" else 0

    # Final feature order (must match training)
    df = df[
        [
            "amount",
            "oldbalanceOrg",
            "newbalanceOrig",
            "oldbalanceDest",
            "newbalanceDest",
            "balanceDiffOrig",
            "balanceDiffDest",
            "type_CASH_OUT",
            "type_DEBIT",
            "type_PAYMENT",
            "type_TRANSFER"
        ]
    ]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠ Fraudulent Transaction Detected (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Legitimate Transaction (Fraud Probability: {probability:.2f})")