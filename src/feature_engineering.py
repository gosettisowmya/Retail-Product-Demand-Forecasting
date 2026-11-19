
import pandas as pd
import os


def create_features(df):
    print("\n========== FEATURE ENGINEERING ==========")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Extract date-based features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["week"] = df["date"].dt.isocalendar().week.astype(int)

    # Create seasonal features
    df["week_sin"] = __import__("numpy").sin(2 * __import__("numpy").pi * df["week"] / 52)
    df["week_cos"] = __import__("numpy").cos(2 * __import__("numpy").pi * df["week"] / 52)

    # Convert store and product names into numerical IDs
    df["store_id"] = df["store"].astype("category").cat.codes
    df["product_id"] = df["product"].astype("category").cat.codes

    print("\nNew features created successfully!")
    print("\nDataset columns:")
    print(df.columns.tolist())

    print("\nFeatured dataset preview:")
    print(df.head())

    return df


def main():
    input_file = "data/cleaned_retail_sales.csv"
    output_file = "data/featured_retail_sales.csv"

    if not os.path.exists(input_file):
        print("Cleaned dataset not found!")
        print("Run preprocessing.py first.")
        return

    df = pd.read_csv(input_file)

    featured_df = create_features(df)

    featured_df.to_csv(output_file, index=False)

    print("\nFeature engineering completed successfully!")
    print("Featured dataset saved to:", output_file)


if __name__ == "__main__":
    main()