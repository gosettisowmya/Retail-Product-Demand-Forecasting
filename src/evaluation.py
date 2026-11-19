
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model():

    print("\n========== MODEL EVALUATION ==========")

    data_file = "data/featured_retail_sales.csv"
    model_file = "outputs/demand_model.pkl"

    if not os.path.exists(data_file):
        print("Featured dataset not found!")
        print("Run feature_engineering.py first.")
        return

    if not os.path.exists(model_file):
        print("Trained model not found!")
        print("Run model_training.py first.")
        return

    # Load dataset
    df = pd.read_csv(data_file)

    # Separate features and target
    X = df.drop(columns=["demand", "date"])
    y = df["demand"]

    # Use the same split as training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Load trained model
    model = joblib.load(model_file)

    # Predict demand
    predictions = model.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    # Display results
    print("\nModel Performance:")
    print("---------------------------")
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R2 Score : {r2:.4f}")

    # Save actual vs predicted values
    results = pd.DataFrame({
        "Actual_Demand": y_test.values,
        "Predicted_Demand": predictions
    })

    os.makedirs("outputs", exist_ok=True)

    results.to_csv(
        "outputs/predictions.csv",
        index=False
    )

    print("\nEvaluation completed successfully!")
    print("Predictions saved to outputs/predictions.csv")


if __name__ == "__main__":
    evaluate_model()
