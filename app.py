import streamlit as st
import pandas as pd
import joblib

# ---- Relative path background image ----
st.markdown(
    """
    <style>
    .stApp {
      background-image: url('C:/Users/HOME/OneDrive/Desktop/ai-heart-tool-640x410px.jpeg');
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered",
)

st.markdown("""
<div style='background: linear-gradient(90deg, #00c6ff, #0072ff); padding: 20px; border-radius: 15px; color: white; text-align: center; font-family: Arial, sans-serif; margin-bottom:20px;'>
    <h1>❤️ Welcome to the Heart Disease Predictor!</h1>
    <p style='font-size: 18px; font-weight: 600;'>Personalized companion for heart health insights 🩺💙</p>
</div>
""", unsafe_allow_html=True)

model_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\LR_heart.pkl"
scaler_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\scaler.pkl"
columns_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\columns.pkl"

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    expected_columns = joblib.load(columns_path)
except Exception as e:
    st.error(f"App failed to load model or scaler: {e}")
    st.stop()

st.markdown("""
> 🚀 **Ready to take control of your heart health?**  
> Fill in the form below and get instant, data-driven insights!  
> Wellness is a journey — let's make it meaningful ✨
""")
st.markdown("---")

with st.form("user_data_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 18, 100, 40, help="Your age")
        sex = st.selectbox("Sex", ["M", "F"], help="Biological sex")
        chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
        resting_bp = st.number_input("Resting BP (mmHg)", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    with col2:
        fasting_bs = st.selectbox("Fasting Blood Sugar >120 mg/dL", [0, 1])
        resting_ecg = st.selectbox("Resting ECG Result", ["Normal", "ST", "LVH"])
        max_hr = st.slider("Max Heart Rate Achieved", 60, 220, 150)
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
        oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    submit_btn = st.form_submit_button("💖 Show me my Heart Risk!")

if submit_btn:
    user_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        f'Sex_{sex}': 1,
        f'ChestPainType_{chest_pain}': 1,
        f'RestingECG_{resting_ecg}': 1,
        f'ExerciseAngina_{exercise_angina}': 1,
        f'ST_Slope_{st_slope}': 1
    }

    input_df = pd.DataFrame([user_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]

    try:
        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]
        proba = model.predict_proba(scaled_input)[0][prediction]
        st.markdown("---")
        if prediction == 1:
            st.markdown("""
                <div style='background-color:#FFD1D1; padding:18px; border-radius:11px; border-left:7px solid #ff3131; margin-top:14px;'>
                <h2 style='color:#a12009;'>🚨 High Risk Detected!</h2>
                <p style='font-size:15px;'>Your prediction suggests <strong>high risk</strong> of heart complications.<br>
                <b>Confidence level:</b> {:.2f}%<br>
                Please consult a cardiologist and maintain a healthy lifestyle!<br>Stay strong 💪 and stay proactive 💡
                </p>
                </div>
            """.format(proba*100), unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='background-color:#D1F7FF; padding:18px; border-radius:11px; border-left:7px solid #00a8ff; margin-top:14px;'>
                <h2 style='color:#0072ff;'>✅ Low Risk – Great Job!</h2>
                <p style='font-size:15px;'>Your heart condition appears <strong>normal</strong>.<br>
                <b>Confidence level:</b> {:.2f}%<br>
                Keep up your healthy habits!<br>Smile more and enjoy life 😄💓
                </p>
                </div>
            """.format(proba*100), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#888888; font-style: italic; margin-top: 48px;">
    Made with ❤️ by Gauransh — Keep your heart smiling! 😄💓  
    <br>
    <span style="font-size:15px;">Feedback welcomed | Stay heart-smart! 💡📬</span>
</div>
""", unsafe_allow_html=True)
