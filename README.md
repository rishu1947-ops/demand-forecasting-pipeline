# End-to-End Demand Forecasting Pipeline

This project implements a production-grade demand forecasting system using XGBoost, MySQL, and FastAPI, fully containerized with Docker.

## Features
- **ETL Pipeline:** Automated ingestion of 900k+ records into a Dockerized MySQL instance.
- **SQL Feature Engineering:** Relational logic to generate Lag features and rolling averages.
- **ML Model:** XGBoost Regressor with Log-Transformation (achieving ~12% MAPE).
- **REST API:** FastAPI wrapper for real-time inference.
- **Containerization:** Fully Dockerized stack for easy deployment.

## 🛠️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Start MySQL via Docker: `docker run ...` (paste your command here)
3. Run scripts 1 through 4 in order.
4. Build Docker image: `docker build -t demand-app .`