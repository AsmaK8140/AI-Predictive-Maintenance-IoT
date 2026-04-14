import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    # Load data
    df = pd.read_csv("data/iot_sensor_data.csv")

    # Features & Target
    X = df[['temperature', 'vibration', 'current']]
    y = df['failure']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(n_estimators=100)

    # Train
    model.fit(X_train, y_train)

    print("✅ Model trained successfully!")

    # Save model
    joblib.dump(model, "models/predictive_maintenance_model.pkl")
    print("💾 Model saved in models/ folder")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()