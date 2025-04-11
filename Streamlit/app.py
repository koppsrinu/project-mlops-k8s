import streamlit as st
import requests

st.title("📊 Real-Time Price Predictor (K8s)")

feature1 = st.number_input("Feature 1 (e.g., Marketing Spend)", value=25000)
feature2 = st.number_input("Feature 2 (TV Ads)", value=5)
feature3 = st.number_input("Feature 3 (Influencer Score)", value=0.85)

if st.button("Predict"):
    data = {
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3
    }

    # Replace with your NodePort endpoint
    response = requests.post("http://192.168.49.2:30036/predict", json=data)

    if response.status_code == 200:
        st.success(f"📈 Predicted Price: {response.json()['prediction']}")
    else:
        st.error("❌ Failed to get prediction.")
