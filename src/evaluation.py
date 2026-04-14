import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/iot_sensor_data.csv")

# Features & Target
X = df[['temperature', 'vibration', 'current']]
y = df['failure']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("models/predictive_maintenance_model.pkl")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Accuracy: {accuracy:.2f}")

# Confusion Matrix
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\n📄 Classification Report:")
print(classification_report(y_test, y_pred))