❤️ Heart Disease Prediction App

A Machine Learning–powered web application for predicting heart disease risk.

This project uses Streamlit, Logistic Regression, and PKL model files to analyze key medical parameters such as age, blood pressure, cholesterol levels, ECG results, and more.
The app provides risk prediction along with a confidence score for better interpretation.

🚀 Features

🧠 Machine Learning Model: Logistic Regression

📂 Loads Model, Scaler & Feature Columns from .pkl files

🎨 Modern & User-Friendly UI built with Streamlit

📊 Displays prediction results + probability score

⚠️ For educational and awareness purposes only

📁 Project Structure

Heart-Disease-Prediction-App/
│── app.py
│── LR_heart.pkl
│── scaler.pkl
│── columns.pkl
│── requirements.txt
│── README.md

🏗️ How It Works

- User enters health parameters into the Streamlit form

- App converts categorical inputs into one-hot encoded values

- Inputs are scaled using the saved StandardScaler

Logistic Regression model predicts:

1 → High Risk of Heart Disease

0 → Low Risk of Heart Disease


🔧 Requirements

All required packages are listed in requirements.txt:

streamlit
numpy
pandas
scikit-learn
joblib

🧠 Model Files (PKL)

This project uses the following saved models:

LR_heart.pkl → Trained Logistic Regression model

scaler.pkl → StandardScaler used during training

columns.pkl → Expected input feature column list

➡️ Important: These files must be in the same folder as app.py.

🌐 Deployment

You can deploy this application easily on:

Streamlit Cloud

HuggingFace Spaces

Render

GitHub Codespaces

(If you want deployment help, just ask!)

👨‍💻 Author

Gauransh Pawar (Akarsh)
Made with ❤️ using Python, Machine Learning, and Streamlit
