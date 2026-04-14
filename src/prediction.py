import joblib
import pandas as pd

model = joblib.load("models/predictive_maintenance_model.pkl")

def predict_failure(temperature, vibration, current):
    data = pd.DataFrame({
        'temperature': [temperature],
        'vibration': [vibration],
        'current': [current]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        print("⚠️ ALERT: Machine Failure Predicted!")
    else:
        print("✅ Machine is operating normally.")