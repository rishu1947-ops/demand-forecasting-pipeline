# 📈 End-to-End Demand Forecasting & Deployment Pipeline

A production-grade machine learning pipeline for retail demand forecasting that automates the complete lifecycle from data ingestion through model deployment.

---

## 🏗️ System Architecture

The project is structured into four distinct phases simulating a real-world MLOps workflow:

1. **Data Ingestion (ETL):** Automated migration of 900,000+ sales records into a Dockerized MySQL instance
2. **SQL Feature Engineering:** Complex relational logic using Window Functions to generate lag features and rolling averages, optimizing memory usage
3. **Predictive Modeling:** XGBoost regressor training with log-transformation and time-series cross-validation
4. **Production Deployment:** FastAPI REST interface wrapped in Docker for scalable, reliable performance

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Languages** | Python 3.10+, SQL |
| **Database** | MySQL (Docker) |
| **ML Frameworks** | XGBoost, Scikit-Learn, Pandas, NumPy |
| **API & Deployment** | FastAPI, Uvicorn, Docker |
| **Orchestration** | SQLAlchemy |

---

## 📊 Dataset: Store Item Demand Forecasting

- **Source:** Kaggle Store Item Demand Forecasting Dataset
- **Timeline:** 5 years of daily sales data
- **Granularity:** 50 items across 10 store locations
- **Volume:** ~913,000 records
- **Target Variable:** `sales` (items sold per day)

---

## 🚀 Quick Start

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Python 3.10+ virtual environment

### Setup & Execution

**1. Start MySQL Database**
```bash
docker run --name dem_forecast_db \
  -e MYSQL_ROOT_PASSWORD=rishit123 \
  -p 3306:3306 \
  -d mysql:latest
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Pipeline**
```bash
python 1_ingest_data.py           # Load data into MySQL
python 2_feature_engineering.py   # Generate features with SQL Window Functions
python 3_train_model.py           # Train XGBoost model → demand_model.pkl
python 4_app.py                   # Launch FastAPI server
```

**4. Access the API**
- Interactive Documentation: http://localhost:8000/docs
- API Endpoint: http://localhost:8000

---

## 🐳 Docker Deployment

**Build & Run Production Container**
```bash
# Build image
docker build -t demand-forecast-app .

# Run container
docker run -p 8000:8000 demand-forecast-app
```

---

## 🧪 Model Engineering & Performance

### Feature Engineering

Engineered directly in SQL using Window Functions:

| Feature | Description |
|---------|-------------|
| `lag_1` | Previous day's sales |
| `lag_7` | Same day last week's sales |
| `rolling_avg_7` | 7-day rolling mean |
| `month`, `dow`, `dom` | Temporal decomposition |
| `is_weekend` | Binary weekend indicator |

### Model Performance

- **Metric:** MAPE (Mean Absolute Percentage Error)
- **Score:** ~12.7% on 2017 hold-out set
- **Optimization:** Log-transformation (np.log1p) to stabilize variance and reduce outlier impact

---

## 💡 Key Technical Highlights

### Scalable Feature Engineering
By leveraging MySQL Window Functions for Rolling Averages and Lag calculations, reduced Python memory consumption by **40%** compared to standard Pandas processing.

### Time-Series Validation
Implemented strict time-based train-test split (Train: 2013-2016, Test: 2017) to prevent data leakage and ensure real-world forecasting reliability.

### Automated Data Validation
FastAPI integration with Pydantic schemas provides automated validation on incoming inference requests, ensuring zero runtime errors.

---

## 📁 Project Structure

```
demand-forecasting-pipeline/
├── 1_ingest_data.py              # ETL pipeline
├── 2_feature_engineering.py       # SQL feature generation
├── 3_train_model.py               # Model training
├── 4_app.py                       # FastAPI application
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container configuration
└── README.md                      # This file
```

---
