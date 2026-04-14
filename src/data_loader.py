import pandas as pd

def load_data(path):
    try:
        data = pd.read_csv(path)
        print("✅ Data loaded successfully!")
        print(data.head())
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None


if __name__ == "__main__":
    df = load_data("data/iot_sensor_data.csv")