📈 End-to-End Demand Forecasting & Deployment Pipeline
This repository contains a production-ready machine learning pipeline for retail demand forecasting. The system automates the journey from raw data ingestion in MySQL to a containerized FastAPI inference service, utilizing XGBoost for high-precision time-series prediction.
🏗️ System Architecture
The project is structured into four distinct phases to simulate a real-world MLOps workflow:
Data Ingestion (ETL): Automated migration of 900,000+ sales records into a Dockerized MySQL database.
SQL Feature Engineering: Execution of complex relational logic (Window Functions) within the database to generate lag features and rolling averages, reducing memory overhead in Python.
Predictive Modeling: Training an optimized XGBoost regressor using log-transformation and time-series cross-validation.
Production Deployment: Wrapping the model in a FastAPI REST interface and containerizing the stack with Docker for scalable deployment.
🛠️ Tech Stack
Languages: Python 3.10+, SQL
Database: MySQL (Dockerized)
ML Frameworks: XGBoost, Scikit-Learn, Pandas, NumPy
API & Deployment: FastAPI, Uvicorn, Docker
Orchestration: SQLAlchemy (Python-SQL bridge)
📊 Dataset: Store Item Demand Forecasting
The project utilizes the Kaggle Store Item Demand Forecasting dataset, which includes:
Timeline: 5 years of daily sales data.
Granularity: 50 different items across 10 distinct store locations.[1][2][3]
Volume: ~913,000 records.
Target Variable: sales (integer count of items sold).
🚀 Getting Started
1. Prerequisites
Docker Desktop installed and running.
Python 3.10+ virtual environment.
2. Setup Infrastructure
Start the MySQL database container:
code
Bash
docker run --name dem_forecast_db -e MYSQL_ROOT_PASSWORD=rishit123 -p 3306:3306 -d mysql:latest
3. Installation
code
Bash
pip install -r requirements.txt
[3][4]
4. Execution Pipeline
Run the scripts in sequence to build the system:
python 1_ingest_data.py: Ingest raw data into MySQL.
python 2_feature_engineering.py: Generate SQL features (Lags, Rolling Averages).
python 3_train_model.py: Train and save the XGBoost model.
python 4_app.py: Spin up the FastAPI server locally.
🧪 Model Performance & Features
Feature Engineering Logic:
To capture seasonality and trends, the following features were engineered:
Lags: lag_1 (yesterday's sales), lag_7 (same day last week).
Rolling Windows: 7-day moving average of sales.
Temporal Features: Month, Day of Week, Is_Weekend, Day of Month.
Performance:
Evaluation Metric: MAPE (Mean Absolute Percentage Error).
Result: Achieved a MAPE of ~12.7% on the 2017 test set.
Optimization: Utilized Log-Transformation (np.log1p) on the target variable to normalize the distribution and improve prediction accuracy for low-volume items.
🐳 Docker Deployment
To build and run the production-grade container:
code
Bash
# Build image
docker build -t demand-forecast-app .

# Run container
docker run -p 8000:8000 demand-forecast-app
The API will be available at http://localhost:8000/docs via Swagger UI.
🧠 Key Takeaways for Interviews
Why MySQL for Feature Engineering? Moving the calculation of rolling averages to the database layer significantly reduces the memory footprint of the Python environment, allowing the system to scale to millions of records.
Why XGBoost? XGBoost handles tabular data effectively and can capture complex non-linear relationships in seasonal demand that traditional ARIMA models might miss.
Why Log-Transformation? Sales data is often right-skewed. Taking the log of the target variable helps the model treat percentage errors equally across low and high-volume items.
