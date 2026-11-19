
import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def train_model():

    print("\n========== MODEL TRAINING ==========")

    file_path = "data/featured_retail_sales.csv"

    if not os.path.exists(file_path):
        print("Featured dataset not found!")
        print("Run feature_engineering.py first.")
        return

    # Load dataset
    df = pd.read_csv(file_path)

    print("Dataset shape:", df.shape)

    # Separate target variable
    y = df["demand"]

    # Remove target and date from input features
    X = df.drop(columns=["demand", "date"])

    # Convert text columns into numerical columns
    X = pd.get_dummies(X, drop_first=False)

    print("\nFeatures after encoding:")
    print(X.head())

    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining data:", X_train.shape)
    print("Testing data:", X_test.shape)

    # Create Random Forest model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    # Train model
    print("\nTraining model...")

    model.fit(X_train, y_train)

    # Create output directory
    os.makedirs("outputs", exist_ok=True)

    # Save trained model
    joblib.dump(model, "outputs/demand_model.pkl")

    # Save feature column names for future prediction
    joblib.dump(X.columns.tolist(), "outputs/model_features.pkl")

    print("\nModel training completed successfully!")
    print("Model saved to outputs/demand_model.pkl")
    print("Feature list saved to outputs/model_features.pkl")


if __name__ == "__main__":
    train_model()
