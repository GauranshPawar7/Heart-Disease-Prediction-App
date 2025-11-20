import joblib
import numpy as np
import pandas as pd

print("Script is running...")  # CONFIRM THIS LINE IS PRESENT

model_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\LR_heart.pkl"
scaler_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\scaler.pkl"
columns_path = r"C:\Users\HOME\OneDrive\Desktop\Python\Model\columns.pkl"

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    columns = joblib.load(columns_path)
    print("All files loaded successfully!")
    print("Expected columns:", columns)
except Exception as e:
    print("Error loading files:", e)
    exit(1)

dummy = {c: 0 for c in columns}
dummy_df = pd.DataFrame([dummy])

try:
    dummy_scaled = scaler.transform(dummy_df)
    pred = model.predict(dummy_scaled)
    print("Prediction on dummy input:", pred)
except Exception as ex:
    print("Error using model/scaler:", ex)
