
import pandas as pd
import os


def preprocess_data(df):

    print("\n========== DATA PREPROCESSING ==========")

    # 1. Display original dataset information
    print("\nOriginal dataset shape:", df.shape)

    # 2. Convert date column into datetime format
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 3. Remove duplicate records
    df = df.drop_duplicates()

    # 4. Handle missing values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    df = df.dropna()

    # 5. Validate data
    df = df[df["price"] > 0]
    df = df[df["demand"] >= 0]

    # 6. Sort records by date
    df = df.sort_values(by="date")

    # 7. Reset index
    df = df.reset_index(drop=True)

    # 8. Display cleaned dataset information
    print("\nCleaned dataset shape:", df.shape)

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print("\nCleaned data preview:")
    print(df.head())

    return df


def main():

    input_file = "data/retail_sales.csv"
    output_file = "data/cleaned_retail_sales.csv"

    if not os.path.exists(input_file):
        print("Dataset not found!")
        print("Run data_generation.py first.")
        return

    # Load generated dataset
    df = pd.read_csv(input_file)

    # Preprocess dataset
    cleaned_df = preprocess_data(df)

    # Save cleaned data
    cleaned_df.to_csv(output_file, index=False)

    print("\nPreprocessing completed successfully!")
    print("Cleaned dataset saved to:", output_file)


if __name__ == "__main__":
    main()
