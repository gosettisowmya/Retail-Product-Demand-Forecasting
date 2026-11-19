
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📦",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    color: #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📦 Retail Product Demand Forecasting")
st.write("Machine Learning dashboard for analyzing retail sales and product demand.")

st.divider()

# ---------------- LOAD DATA ----------------
DATA_FILE = "data/featured_retail_sales.csv"

if not os.path.exists(DATA_FILE):
    st.error("Dataset not found. Please run your data pipeline first.")
    st.code("python src/data_generation.py\npython src/preprocessing.py\npython src/feature_engineering.py")
    st.stop()

df = pd.read_csv(DATA_FILE)

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "demand"])

# ---------------- SIDEBAR ----------------
st.sidebar.header("Dashboard Filters")

stores = ["All Stores"] + sorted(df["store"].astype(str).unique().tolist())
products = ["All Products"] + sorted(df["product"].astype(str).unique().tolist())

selected_store = st.sidebar.selectbox("Select Store", stores)
selected_product = st.sidebar.selectbox("Select Product", products)

filtered_df = df.copy()

if selected_store != "All Stores":
    filtered_df = filtered_df[
        filtered_df["store"].astype(str) == selected_store
    ]

if selected_product != "All Products":
    filtered_df = filtered_df[
        filtered_df["product"].astype(str) == selected_product
    ]

# ---------------- KPI METRICS ----------------
st.subheader("📊 Key Performance Indicators")

total_demand = filtered_df["demand"].sum()
average_demand = filtered_df["demand"].mean()
total_records = len(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Demand", f"{total_demand:,.0f} units")
col2.metric("Average Demand", f"{average_demand:,.2f} units")
col3.metric("Sales Records", f"{total_records:,}")

st.divider()

# ---------------- DEMAND TREND ----------------
st.subheader("📈 Weekly Demand Trend")

weekly_demand = (
    filtered_df.groupby("date")["demand"]
    .sum()
    .reset_index()
    .sort_values("date")
)

st.line_chart(
    weekly_demand.set_index("date")["demand"],
    use_container_width=True
)

# ---------------- STORE ANALYSIS ----------------
st.subheader("🏪 Store-wise Demand")

store_demand = (
    filtered_df.groupby("store")["demand"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(store_demand, use_container_width=True)

# ---------------- PRODUCT ANALYSIS ----------------
st.subheader("📦 Top 10 Products by Demand")

product_demand = (
    filtered_df.groupby("product")["demand"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(product_demand, use_container_width=True)

# ---------------- PRICE ANALYSIS ----------------
if "price" in filtered_df.columns:
    st.subheader("💰 Price Analysis")

    price_demand = (
        filtered_df.groupby("price")["demand"]
        .mean()
        .reset_index()
        .sort_values("price")
    )

    st.line_chart(
        price_demand.set_index("price")["demand"],
        use_container_width=True
    )

# ---------------- PROMOTION ANALYSIS ----------------
if "promotion" in filtered_df.columns:
    st.subheader("🎯 Promotion Analysis")

    promotion_demand = (
        filtered_df.groupby("promotion")["demand"]
        .mean()
    )

    st.bar_chart(promotion_demand)

# ---------------- DATA TABLE ----------------
st.subheader("📋 Retail Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

st.success("Dashboard loaded successfully!")
