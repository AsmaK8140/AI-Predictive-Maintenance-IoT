import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_features(df):
    # Features (Input)
    X = df[['temperature', 'vibration', 'current']]

    # Target (Output)
    y = df['failure']

    print("\n📊 Features (X):")
    print(X.head())

    print("\n🎯 Target (y):")
    print(y.head())

    return X, y


def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\n✅ Data split completed!")
    print(f"Training size: {len(X_train)}")
    print(f"Testing size: {len(X_test)}")

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    df = pd.read_csv("data/iot_sensor_data.csv")

    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)