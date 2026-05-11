import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('rf_best_model.pkl')

# App title
st.title("Fetal Health Prediction App")

st.write("Enter CTG values to predict fetal health state.")

# Input fields
LB = st.number_input("Baseline FHR (LB)", value=120.0)
AC = st.number_input("Accelerations (AC)", value=0.0)
FM = st.number_input("Fetal Movement (FM)", value=0.0)
UC = st.number_input("Uterine Contractions (UC)", value=0.0)
ASTV = st.number_input("ASTV", value=0.0)
MSTV = st.number_input("MSTV", value=0.0)
ALTV = st.number_input("ALTV", value=0.0)
MLTV = st.number_input("MLTV", value=0.0)
Width = st.number_input("Width", value=0.0)
Min = st.number_input("Min", value=0.0)
Max = st.number_input("Max", value=0.0)
Nmax = st.number_input("Nmax", value=0.0)
Nzeros = st.number_input("Nzeros", value=0.0)
Mode = st.number_input("Mode", value=0.0)
Mean = st.number_input("Mean", value=0.0)
Median = st.number_input("Median", value=0.0)
Variance = st.number_input("Variance", value=0.0)
Tendency = st.number_input("Tendency", value=0.0)

# Prediction button
if st.button("Predict"):

    input_data = np.array([[
        LB, AC, FM, UC, ASTV, MSTV,
        ALTV, MLTV, Width, Min,
        Max, Nmax, Nzeros, Mode,
        Mean, Median, Variance, Tendency
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: Normal")
    elif prediction[0] == 2:
        st.warning("Prediction: Suspect")
    else:
        st.error("Prediction: Pathologic")