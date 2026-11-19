
# 🛒 Retail Product Demand Forecasting

## 📌 Project Overview

Retail Product Demand Forecasting is a Machine Learning project that predicts weekly product demand across multiple retail stores.

Retail businesses often face problems such as stockouts and excess inventory due to inaccurate demand forecasting. This project uses historical sales patterns, pricing, promotions, and seasonal trends to predict product demand and support better inventory management decisions.

## 🎯 Objectives

- Predict weekly demand for retail products.
- Identify important demand drivers.
- Analyze seasonal demand patterns.
- Reduce stockouts and excess inventory.
- Support data-driven inventory planning.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- VS Code
- Git & GitHub

## 📂 Project Structure

```text
Retail-Product-Demand-Forecasting/
│
├── data/
│   ├── retail_sales.csv
│   ├── cleaned_retail_sales.csv
│   └── featured_retail_sales.csv
│
├── outputs/
│
├── src/
│   ├── data_generation.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore

```

## ⚙️ Project Workflow

1. Data Generation
2. Data Preprocessing
3. Feature Engineering
4. Machine Learning Model Training
5. Model Evaluation
6. Data Visualization

## 📊 Dataset Description

The dataset contains retail sales information generated for multiple stores and products.

| Feature | Description |
|---|---|
| date | Date of sales record |
| store | Store identifier |
| product | Product identifier |
| price | Product price |
| promotion | Promotional indicator |
| holiday | Holiday indicator |
| demand | Product demand |

## 🤖 Machine Learning Algorithm

The project uses regression-based machine learning techniques to predict weekly product demand.

Planned model:
- Random Forest Regressor

The model learns patterns from product pricing, promotions, seasonal trends, and store/product information.

## 📈 Evaluation Metrics

The model performance is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 💡 Expected Benefits

- Improved demand forecasting
- Better inventory management
- Reduced stockout risk
- Reduced overstocking
- Better understanding of seasonal sales patterns

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/gosettisowmya/Retail-Product-Demand-Forecasting.git
```

### 2. Navigate to the project folder

```bash
cd Retail-Product-Demand-Forecasting
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the dataset

```bash
python src/data_generation.py
```

### 5. Preprocess the dataset

```bash
python src/preprocessing.py
```

### 6. Perform feature engineering

```bash
python src/feature_engineering.py
```

### 7. Train the model

```bash
python src/model_training.py
```

### 8. Evaluate the model

```bash
python src/evaluation.py
```

## 🔮 Future Enhancements

- Interactive Streamlit dashboard
- Demand forecasting for individual products
- Store-wise demand analysis
- Advanced time-series forecasting models
- Automated inventory recommendations

## 👩‍💻 Author

**Gosetti Sowmya**

B.Tech – Computer Science and Engineering (Data Science)

GitHub: [gosettisowmya](https://github.com/gosettisowmya)

---

⭐ If you find this project useful, feel free to explore the repository.

