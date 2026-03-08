# fraud_Detection
Analyzes financial transactions to identify zero-balance transfers and cash-outs, highlighting suspicious or edge-case behaviors

dataset:- 
https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download


Fraud Detection ML System
1. Project Overview

Fraud Detection ML System – A machine learning application that identifies high-risk financial transactions using behavioral patterns in transaction data. The system helps financial institutions detect fraudulent activities early and reduce potential financial losses.

The model analyzes transaction features such as transaction amount, account balance changes, and transaction type to classify transactions as legitimate or fraudulent.

2. Business Problem

Digital banking and online payments have significantly increased transaction volume. However, this growth also increases exposure to fraud.

Financial institutions face challenges such as:

Unauthorized transfers

Account takeovers

Suspicious high-value transactions

Traditional rule-based systems struggle to detect sophisticated fraud patterns.

This project builds a machine learning fraud detection system capable of identifying suspicious transactions automatically.

3. Dataset Description

The dataset contains millions of financial transaction records representing various types of digital payments.

Dataset Characteristics

Property	Value
Transactions	~6.3 million
Features	11
Target Variable	isFraud

Important Features

Feature	Description
amount	Transaction value
type	Transaction category
oldbalanceOrg	Sender balance before transaction
newbalanceOrig	Sender balance after transaction
oldbalanceDest	Receiver balance before transaction
newbalanceDest	Receiver balance after transaction

Feature Engineering

Additional features were created:

balanceDiffOrig

balanceDiffDest

These help detect abnormal balance changes during transactions.

4. Data Processing Pipeline

The machine learning pipeline includes:

Data cleaning

Feature engineering

Handling class imbalance using imbalanced-learn SMOTE

Feature encoding using **scikit-learn preprocessing tools

Model training

Fraud datasets are highly imbalanced (fraud cases are very rare), so SMOTE was used to generate synthetic fraud samples for training.

5. Model Development

The final model uses XGBoost, a gradient boosting algorithm widely used in financial risk modeling.

Reasons for choosing XGBoost:

Handles imbalanced datasets well

Strong performance on tabular financial data

Captures nonlinear relationships

Robust against noisy features

The model was trained using engineered features and optimized parameters.

6. Model Performance

Performance was evaluated using classification metrics commonly used in fraud detection.

Metric	Score
Accuracy	~99%
Precision	0.90
Recall	0.92
F1 Score	0.91
ROC-AUC	0.98
Key Insight

Recall of 92% means the system successfully identifies 92% of fraudulent transactions, significantly reducing undetected fraud risk.

7. Business Impact

Implementing this fraud detection model can help financial institutions:

Detect fraudulent transactions in real time

Prevent unauthorized fund transfers

Reduce operational losses

Improve transaction monitoring systems

Even a small improvement in fraud detection accuracy can save millions in financial losses annually.

8. Interactive Fraud Detection Dashboard

An interactive web application was built using Streamlit.

The dashboard allows users to:

Input transaction details

Predict fraud risk instantly

View fraud probability scores

This demonstrates how machine learning models can be integrated into real-world financial monitoring systems.

9. Key Insights from Analysis

Exploratory analysis revealed several fraud patterns:

Fraud frequently occurs in TRANSFER and CASH_OUT transactions

Fraudulent transactions often involve large sudden balance changes

Many fraud cases occur when sender balances drop to zero after transfer

These insights help financial institutions understand fraud behavior patterns.

10. Future Improvements

Potential improvements include:

Real-time transaction monitoring

Graph-based fraud detection

Deep learning models for behavioral analysis

Integration with banking transaction systems

Skills Demonstrated

Machine Learning

Fraud Detection Modeling

Feature Engineering

Data Analysis

Model Deployment

Interactive Dashboard Development

Tools used:

Python

scikit-learn

XGBoost

Streamlit

pandas

matplotlib
