import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Predictive Maintenance", layout="wide")

st.title("🔧 AI Predictive Maintenance Dashboard")

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("models/predictive_maintenance_model.pkl")

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("data/iot_sensor_data.csv")

# -------------------------------
# KPI METRICS (NEW ✅)
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Total Records", len(df))

with col2:
    st.metric("⚠️ Failure Cases", df['failure'].sum())

with col3:
    failure_rate = round((df['failure'].sum() / len(df)) * 100, 2)
    st.metric("📉 Failure Rate (%)", f"{failure_rate}%")

st.markdown("---")

# -------------------------------
# LAYOUT: LEFT (TABLE) | RIGHT (INPUT + RESULT)
# -------------------------------
left_col, right_col = st.columns(2)

# -------------------------------
# LEFT SIDE → DATASET
# -------------------------------
with left_col:
    st.subheader("📊 Dataset Preview")
    st.dataframe(df)

# -------------------------------
# RIGHT SIDE → INPUT + PREDICTION
# -------------------------------
with right_col:
    st.subheader("⚙️ Input Sensor Values")

    temperature = st.slider("Temperature", 30, 100, 50)
    vibration = st.slider("Vibration", 0.0, 10.0, 2.0)
    current = st.slider("Current", 5.0, 20.0, 10.0)

    if st.button("Predict"):

        input_data = np.array([[temperature, vibration, current]])
        prediction = model.predict(input_data)[0]

        st.subheader("📈 Prediction Result")

        # -------------------------------
        # BUSINESS LOGIC (NEW ✅)
        # -------------------------------
        if prediction == 1:
            st.error("⚠️ Machine Failure Predicted!")
            st.write("🔧 Suggested Action: Inspect motor, cooling system, and vibration levels.")
        else:
            st.success("✅ Machine is Operating Normally")
            st.write("🟢 No immediate action required.")

# -------------------------------
# VISUALIZATIONS (BIGGER + BELOW)
# -------------------------------
st.markdown("---")
st.subheader("📈 Sensor vs Failure Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['temperature'], df['failure'])
    ax.set_title("Temperature vs Failure")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Failure")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['vibration'], df['failure'])
    ax.set_title("Vibration vs Failure")
    ax.set_xlabel("Vibration")
    ax.set_ylabel("Failure")
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['current'], df['failure'])
    ax.set_title("Current vs Failure")
    ax.set_xlabel("Current")
    ax.set_ylabel("Failure")
    st.pyplot(fig)