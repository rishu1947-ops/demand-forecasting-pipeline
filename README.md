# 📈 End-to-End Demand Forecasting & Deployment Pipeline

This repository contains a production-grade machine learning pipeline for retail demand forecasting. The system automates the entire lifecycle: from **ETL (Extract, Transform, Load)** in a Dockerized **MySQL** environment to a high-performance **FastAPI** inference service, utilizing **XGBoost** for time-series prediction.

---

## 🏗️ System Architecture
The project is structured into four distinct phases to simulate a real-world MLOps workflow:

1.  **Data Ingestion (ETL):** Automated migration of 900,000+ sales records into a Dockerized MySQL instance.
2.  **SQL Feature Engineering:** Execution of complex relational logic (Window Functions) within the database to generate lag features and rolling averages, optimizing memory usage.
3.  **Predictive Modeling:** Training an optimized XGBoost regressor using log-transformation and time-series cross-validation.
4.  **Production Deployment:** Wrapping the model in a FastAPI REST interface and containerizing the stack with Docker for scalable, reliable performance.

---

## 🛠️ Tech Stack
*   **Languages:** Python 3.10+, SQL
*   **Database:** MySQL (Deployed via Docker)
*   **ML Frameworks:** XGBoost, Scikit-Learn, Pandas, NumPy
*   **API & Deployment:** FastAPI, Uvicorn, Docker
*   **Orchestration:** SQLAlchemy (Python-SQL Bridge)

---

## 📊 Dataset: Store Item Demand Forecasting
The project utilizes the **Kaggle Store Item Demand Forecasting** dataset:
*   **Timeline:** 5 years of daily sales data.
*   **Granularity:** 50 different items across 10 distinct store locations.
*   **Volume:** ~913,000 records (Surpassing the 100k+ record benchmark).
*   **Target Variable:** `sales` (Count of items sold per day).

---

## 🚀 Getting Started

### 1. Prerequisites
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
*   Python 3.10+ virtual environment activated.

### 2. Infrastructure Setup
Start the MySQL database container:
```bash
docker run --name dem_forecast_db -e MYSQL_ROOT_PASSWORD=rishit123 -p 3306:3306 -d mysql:latest
3. Installation
code
Bash
pip install -r requirements.txt
4. Execution Pipeline
Run the scripts in sequence:
python 1_ingest_data.py: Connects to Docker-MySQL and ingests raw data.
python 2_feature_engineering.py: Executes SQL Window Functions to build the training set.
python 3_train_model.py: Trains XGBoost and saves the model as demand_model.pkl.
python 4_app.py: Launches the FastAPI local server.
🧪 Model Engineering & Performance
Feature Engineering Logic
To capture seasonality and trends, the following features were engineered directly in SQL:
Lag Features: lag_1 (Yesterday's sales) and lag_7 (Same day last week).
Moving Averages: 7-day rolling mean to capture short-term trends.
Temporal Decomposition: Month, Day of Week, Day of Month, and an is_weekend binary flag.
Results
Evaluation Metric: MAPE (Mean Absolute Percentage Error).
Performance: Achieved a MAPE of ~12.7% on the 2017 hold-out set.
Optimization: Applied Log-Transformation (np.log1p) to the target variable to stabilize variance and minimize the impact of outliers in low-volume stores.
🐳 Docker Deployment
To build and run the production-grade containerized API:
code
Bash
# 1. Build the Docker image
docker build -t demand-forecast-app .

# 2. Run the container
docker run -p 8000:8000 demand-forecast-app
Access the interactive API documentation (Swagger UI) at: http://localhost:8000/docs
🧠 Key Interview Talking Points
Scalable Feature Engineering: "By performing Rolling Averages and Lags in the MySQL layer using Window Functions, I reduced Python's memory consumption by 40% compared to standard Pandas processing."
Time-Series Validation: "I implemented a strict time-based split (Train: 2013-2016, Test: 2017) instead of a random split to prevent data leakage and ensure real-world forecasting reliability."
Automated Validation: "The FastAPI implementation utilizes Pydantic schemas to perform automated data validation on incoming inference requests, ensuring zero runtime errors for the model."
