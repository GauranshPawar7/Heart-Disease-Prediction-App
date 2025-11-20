
❤️ Heart Disease Prediction App

A Machine Learning web application built using Streamlit, Logistic Regression, and PKL model files.
This app predicts the risk of heart disease based on medical parameters such as age, blood pressure, cholesterol, ECG results, and more.

🚀 Features

🧠 ML Model: Logistic Regression

📂 Loads Model, Scaler & Feature Columns from PKL files

🎨 Modern UI with Streamlit

📊 Displays Prediction + Confidence Score

⚠️ Educational Use Only

📁 Project Structure
Heart-Disease-Prediction-App/
│── app.py
│── LR_heart.pkl
│── scaler.pkl
│── columns.pkl
│── requirements.txt
│── README.md

🏗️ How It Works

User enters medical parameters

App one-hot encodes categorical inputs

Input is scaled using the stored StandardScaler

Logistic Regression model predicts:

1 → High Risk

0 → Low Risk

Confidence score (probability) is displayed

🧪 Demo Screenshots (optional)

Add your screenshots here later

💻 Installation & Running the App
1️⃣ Clone the Project
git clone https://github.com/YOUR-USERNAME/heart-disease-prediction-app.git
cd heart-disease-prediction-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py

🔧 Requirements

Install from requirements.txt:

streamlit
numpy
pandas
scikit-learn
joblib

🧠 Model Files (PKL)

The app uses:

LR_heart.pkl → Logistic Regression Model

scaler.pkl → StandardScaler

columns.pkl → List of expected one-hot encoded columns

Make sure they are placed inside the same folder as app.py.

🌐 Deployment (Optional)

You can deploy on:

Streamlit Cloud

HuggingFace Spaces

GitHub Codespaces

Render

I can help you deploy if you want — just ask!

👨‍💻 Author

Gauransh Pawar (Akarsh)
Made with ❤️ using Python & Streamlit

⚠️ Disclaimer

This app is for educational and awareness purposes only.
It does not replace professional medical advice.
