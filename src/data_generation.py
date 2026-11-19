
import numpy as np
import pandas as pd
import os


def generate_retail_data():

    print("Generating retail sales data...")

    np.random.seed(42)

    stores = [f"Store_{i}" for i in range(1, 6)]
    products = [f"Product_{i}" for i in range(1, 21)]

    dates = pd.date_range(
        start="2023-01-02",
        periods=104,
        freq="W-MON"
    )

    records = []

    for store in stores:

        store_factor = np.random.uniform(0.8, 1.3)

        for product in products:

            product_factor = np.random.uniform(0.7, 1.5)
            base_price = np.random.uniform(50, 500)

            for date in dates:

                week = date.isocalendar().week

                # Seasonal demand
                seasonal_factor = (
                    1 + 0.25 * np.sin(2 * np.pi * week / 52)
                )

                # Holiday effect
                holiday = 1 if week in [1, 25, 47, 48, 51, 52] else 0
                holiday_factor = 1.4 if holiday else 1.0

                # Promotion effect
                promotion = np.random.choice([0, 1], p=[0.75, 0.25])
                promotion_factor = 1.3 if promotion else 1.0

                # Price variation
                price = base_price * np.random.uniform(0.9, 1.1)

                # Calculate demand
                demand = (
                    100
                    * store_factor
                    * product_factor
                    * seasonal_factor
                    * holiday_factor
                    * promotion_factor
                    * (base_price / price)
                )

                # Add random noise
                demand += np.random.normal(0, 10)

                demand = max(0, int(round(demand)))

                records.append({
                    "date": date,
                    "store": store,
                    "product": product,
                    "price": round(price, 2),
                    "promotion": promotion,
                    "holiday": holiday,
                    "demand": demand
                })

    df = pd.DataFrame(records)

    # Save dataset
    os.makedirs("data", exist_ok=True)

    df.to_csv("data/retail_sales.csv", index=False)

    print("Dataset generated successfully!")
    print("Total records:", len(df))
    print(df.head())

    return df


if __name__ == "__main__":
    generate_retail_data()
