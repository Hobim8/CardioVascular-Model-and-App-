import streamlit as st
import pandas as pd
import joblib
import streamlit_authenticator as stauth
import requests
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ---------------------- AUTHENTICATION SETUP ----------------------

# Create hashed password for each user once and store here (pre-generated)

# Hashed password for 'cvd123' generated using stauth.Hasher(['cvd123']).generate()
hashed_password = "$2b$12$lbuCRnsjtzW.d84ZnU64lOMonZm4AaadrIlZkzKPod6WX9dcva7ge"

credentials = {
    "usernames": {
        "user": {
            "name": "Kolade",  # Replace with the actual user's name
            "password": hashed_password  # "cvd123"
        }
    }
}



authenticator = stauth.Authenticate(
    credentials,
    "cvd_app",
    "auth",
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", location = "main")

if authentication_status:
    st.sidebar.success(f"Welcome, {name} 👋")
    authenticator.logout("Logout", "sidebar")

    # ---------------------- MODEL + GOOGLE SHEET SETUP ----------------------

    # Load the trained SVM model
    model = joblib.load("cvd_prediction_model.pkl")

    # ---------------------- INPUT FORM ----------------------

    st.title("🩺 Cardiovascular Disease Risk Predictor")

    with st.form("prediction_form"):
        st.subheader("Enter Patient Details")

        age = st.number_input("Age", 20, 100)
        email = st.text_input("Email Address")
        gender = st.radio("Gender", ["Male", "Female"])
        currently_smokes = st.radio("Currently Smokes?", ["Yes", "No"])
        cigarettes_per_day = st.slider("Cigarettes Per Day", 0, 100)
        bp_medication = st.radio("On BP Medication?", ["Yes", "No"])
        history_of_stroke = st.radio("History of Stroke?", ["Yes", "No"])
        has_hypertension = st.radio("Has Hypertension?", ["Yes", "No"])
        has_diabetes = st.radio("Has Diabetes?", ["Yes", "No"])
        total_cholesterol = st.number_input("Total Cholesterol (mg/dL)", 100, 400)
        systolic_bp = st.number_input("Systolic BP (mmHg)", 90, 200)
        diastolic_bp = st.number_input("Diastolic BP (mmHg)", 60, 130)
        bmi = st.number_input("BMI", 10.0, 50.0)
        glucose_level = st.number_input("Glucose Level (mg/dL)", 60, 300)

        submitted = st.form_submit_button("Check Risk")

    if submitted:
        input_data = pd.DataFrame([{
            "gender": 1 if gender == "Male" else 0,
            "age": age,
            "currently_smokes": 1 if currently_smokes == "Yes" else 0,
            "cigarettes_per_day": cigarettes_per_day,
            "bp_medication": 1 if bp_medication == "Yes" else 0,
            "history_of_stroke": 1 if history_of_stroke == "Yes" else 0,
            "has_hypertension": 1 if has_hypertension == "Yes" else 0,
            "has_diabetes": 1 if has_diabetes == "Yes" else 0,
            "total_cholesterol": total_cholesterol,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp,
            "bmi": bmi,
            "glucose_level": glucose_level
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        # Generate recommendation based on rules
        recommendations = []
        if prediction == 1:
            if systolic_bp > 140:
                recommendations.append("Reduce blood pressure through medication or diet")
            if cigarettes_per_day > 10:
                recommendations.append("Reduce or quit smoking")
            if glucose_level > 110:
                recommendations.append("Check for pre-diabetes or diabetes")
            if bmi > 27:
                recommendations.append("Consider weight management or exercise program")
        else:
            recommendations.append("Maintain your current healthy lifestyle")

        st.subheader("🧠 Prediction Result")
        st.markdown(f"**Risk Level:** {'High' if prediction == 1 else 'Low'}")
        st.markdown(f"**Risk Probability:** {probability * 100:.1f}%")
        st.markdown("---")
        st.subheader("📌 Recommendations")
        for rec in recommendations:
            st.markdown(f"- {rec}")

       # ------------------ LOG TO GOOGLE SHEET ------------------
        webhook_url = "https://script.google.com/macros/s/AKfycbzn08xyprH1K8Fz7SjZs04ijkVcZHPkDV54ZrdKxboGCvhuPV3T3Vl9BR1umI7VA-D_/exec"
        payload = {
            "name": name,
            "email": email,
            "prediction": int(prediction),
            "risk_score": round(probability*100, 2),
            "age": age,
            "gender": gender,
            "smoker": currently_smokes,
            "cigarettes_per_day": cigarettes_per_day,
            "bp_med": bp_medication,
            "diabetes": has_diabetes,
            "hypertension": has_hypertension,
            "glucose": glucose_level,
            "bmi": bmi
        }

        try:
            res = requests.post(webhook_url, json=payload)
            if res.status_code == 200:
                st.success("✅ Data used to make prediction logged into Google Sheet.")
            else:
                st.warning("⚠️ Prediction made, but data used for prediction not logged to Google Sheet.")
        except Exception as e:
            st.error(f"Logging error: {e}")

elif authentication_status is False:
    st.error("❌ Incorrect username or password")
elif authentication_status is None:
    st.warning("Please enter your credentials")