from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

# ---- Load trained model once at startup ----
MODEL_PATH = "demand_model.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Failed to load model:")
    print(e)
    model = None

app = FastAPI(title="Demand Forecasting API")


# ---- Request schema ----
class PredictionInput(BaseModel):
    store: int
    item: int
    month: int
    dayofweek: int
    dayofmonth: int
    is_weekend: int
    lag_1: float
    lag_7: float
    rolling_avg_7d: float


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict")
def predict(payload: PredictionInput):
    if model is None:
        return {"error": "Model not loaded properly."}

    try:
        # Convert request into dataframe (model expects tabular input)
        input_data = pd.DataFrame([payload.model_dump()])

        # Make prediction
        log_pred = model.predict(input_data)

        # Reverse log1p transformation
        final_pred = np.expm1(log_pred)

        return {
            "store": payload.store,
            "item": payload.item,
            "predicted_sales": round(float(final_pred[0]), 2)
        }

    except Exception as e:
        return {"error": str(e)}