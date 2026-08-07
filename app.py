import streamlit as st
import pandas as pd
import pickle
import os

# ---------------- Page config ----------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# ---------------- Load model ----------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ---------------- Header ----------------
if os.path.exists("heart.jpg"):
    st.image("heart.jpg", width=150)

st.title("Heart Disease Prediction")
st.write(
    "Enter the patient's details below. The app uses a Random Forest "
    "model trained on the Heart Disease dataset to predict the risk."
)

st.divider()

# ---------------- Input form ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=52)
    sex = st.selectbox("Sex", options=[1, 0],
                       format_func=lambda x: "Male" if x == 1 else "Female")
    cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3],
                      format_func=lambda x: {
                          0: "0 - Typical angina",
                          1: "1 - Atypical angina",
                          2: "2 - Non-anginal pain",
                          3: "3 - Asymptomatic"
                      }[x])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)",
                               min_value=80, max_value=220, value=130)
    chol = st.number_input("Cholesterol (chol)",
                           min_value=100, max_value=600, value=250)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)",
                       options=[0, 1],
                       format_func=lambda x: "Yes" if x == 1 else "No")
    restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate Achieved (thalach)",
                              min_value=60, max_value=220, value=170)
    exang = st.selectbox("Exercise Induced Angina (exang)",
                         options=[0, 1],
                         format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.number_input("ST Depression (oldpeak)",
                              min_value=0.0, max_value=10.0,
                              value=1.2, step=0.1)
    slope = st.selectbox("Slope of ST Segment (slope)", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (ca)", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (thal)", options=[0, 1, 2, 3])

st.divider()

# ---------------- Prediction ----------------
if st.button("Predict", type="primary", use_container_width=True):
    # Build a DataFrame with the SAME column names used during training
    input_df = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }])

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease (confidence: {proba[1]:.0%})")
    else:
        st.success(f"✅ Low risk of heart disease (confidence: {proba[0]:.0%})")

    st.progress(float(proba[1]),
                text=f"Risk probability: {proba[1]:.0%}")

    st.caption(
        "This prediction is for educational purposes only and is not "
        "a medical diagnosis. Please consult a doctor for real health concerns."
    )
