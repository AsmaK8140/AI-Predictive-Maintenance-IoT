import pandas as pd

def preprocess_data(df):
    print("\n🔍 Checking missing values:")
    print(df.isnull().sum())

    print("\n📊 Data Types:")
    print(df.dtypes)

    # Convert data types (if needed)
    df["temperature"] = df["temperature"].astype(float)
    df["vibration"] = df["vibration"].astype(float)
    df["current"] = df["current"].astype(float)
    df["failure"] = df["failure"].astype(int)

    print("\n✅ Data cleaned successfully!")

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/iot_sensor_data.csv")
    df = preprocess_data(df)
    print(df.head())