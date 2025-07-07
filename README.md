# MLOPS_2# 💎 Gemstone Price Prediction - MLOps Project

This project aims to predict the price of cubic zirconia gemstones using a machine learning pipeline integrated with MLOps best practices. The project demonstrates the complete ML lifecycle, including data processing, model training, and deployment using modern tools like **DVC**, **Git**, **Docker**, and **Airflow**.

---

## 📌 Problem Statement

The goal is to predict the price of gemstones based on features such as carat, cut, clarity, color, and depth using machine learning algorithms. The dataset used is `cubic_zirconia.csv`.

---

## ⚙️ MLOps Workflow

This project follows a modular MLOps architecture involving the following stages:

### 1. 📥 Data Integration
- Raw data collected from `cubic_zirconia.csv`
- Version-controlled with **DVC**
- Tracked using **Git**

### 2. 🔄 Data Transformation
- Handled missing values and categorical encoding
- Normalized numerical features
- Pipelines built with **scikit-learn** transformers

### 3. ✅ Data Validation
- Schema validation using custom validators
- Data quality checks using pandas-profiling and Great Expectations

### 4. 🤖 Model Training & Prediction
- Trained regression models (Linear Regression, Random Forest)
- Evaluated using RMSE, MAE, R² metrics
- Hyperparameter tuning using GridSearchCV

### 5. 🧪 Model Validation
- Tracked with **MLflow**
- Metrics and model artifacts saved via **DVC**

### 6. 🐳 Containerization
- Dockerized the entire application for portability
- Includes training script, prediction API, and dependencies



---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core ML programming |
| **Pandas, NumPy** | Data manipulation |
| **Scikit-learn** | Modeling & evaluation |
| **DVC** | Data & model versioning |
| **Git** | Source code management |
| **Docker** | Containerization |
| **MLflow** | Experiment tracking |


![image](https://github.com/user-attachments/assets/52189fa1-eafd-4961-9b51-5aac0061de95)
![Screenshot 2025-07-07 222423](https://github.com/user-attachments/assets/1c1b2035-f27e-409e-bbdd-586c968ef245)



