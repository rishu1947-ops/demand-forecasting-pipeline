📈 End-to-End Demand Forecasting & Deployment Pipeline

An end-to-end machine learning pipeline for retail demand forecasting — from raw data ingestion in MySQL to a containerized FastAPI inference service.

The project simulates a real-world MLOps workflow including ETL, SQL-based feature engineering, model training with XGBoost, and production deployment using Docker.

🏗️ Project Architecture

The system is divided into four main stages:

1️⃣ Data Ingestion (ETL)

Migrates ~900k+ historical sales records into a Dockerized MySQL database.

Uses SQLAlchemy as a bridge between Python and MySQL.

2️⃣ SQL Feature Engineering

Feature creation is performed directly inside MySQL using window functions:

lag_1 → previous day sales

lag_7 → same day last week

rolling_avg_7d → 7-day moving average

This reduces memory overhead in Python and improves scalability.

3️⃣ Predictive Modeling

Model: XGBoost Regressor

Log transformation applied (np.log1p) to normalize skewed sales data.

Time-aware validation split for realistic evaluation.

4️⃣ Production Deployment

Model wrapped inside a FastAPI REST API.

Containerized using Docker.

Interactive API documentation via Swagger UI.

🛠️ Tech Stack

Languages

Python 3.10+

SQL

Database

MySQL (Dockerized)

Machine Learning

XGBoost

Scikit-Learn

Pandas

NumPy

API & Deployment

FastAPI

Uvicorn

Docker

Database Integration

SQLAlchemy

📊 Dataset

Source: Kaggle – Store Item Demand Forecasting

Details:

5 years of daily sales data

50 items

10 store locations

~913,000 records

Target variable: sales (integer count)

🚀 Getting Started
1️⃣ Prerequisites

Docker Desktop installed and running

Python 3.10+

Virtual environment recommended

2️⃣ Start MySQL Container
docker run --name dem_forecast_db \
  -e MYSQL_ROOT_PASSWORD=rishit123 \
  -p 3306:3306 \
  -d mysql:latest
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Pipeline

Execute scripts in order:

python 1_ingest_data.py
python 2_feature_engineering.py
python 3_train_model.py
python 4_app.py

API will be available at:

http://localhost:8000/docs
🧪 Model Performance

Evaluation Metric:

MAPE (Mean Absolute Percentage Error)

Result:

~12.7% MAPE on 2017 test set

📌 Engineered Features
Lag Features

lag_1

lag_7

Rolling Window

7-day moving average (rolling_avg_7d)

Temporal Features

Month

Day of week

Day of month

Is weekend flag

🐳 Docker Deployment

Build and run the API container:

# Build image
docker build -t demand-forecast-app .

# Run container
docker run -p 8000:8000 demand-forecast-app

Swagger UI:

http://localhost:8000/docs
💡 Design Decisions
Why SQL for Feature Engineering?

Performing lag and rolling window computations inside MySQL:

Reduces Python memory usage

Keeps transformation logic closer to the data

Improves scalability for large datasets

Why XGBoost?

Strong performance on structured/tabular data

Handles non-linear seasonal patterns

Robust to feature interactions

Why Log-Transform the Target?

Retail sales are typically right-skewed.
Applying log1p:

Stabilizes variance

Improves performance on low-volume items

Reduces relative error imbalance

📦 Project Structure
.
├── 1_ingest_data.py
├── 2_feature_engineering.py
├── 3_train_model.py
├── 4_app.py
├── demand_model.pkl
├── requirements.txt
└── Dockerfile
