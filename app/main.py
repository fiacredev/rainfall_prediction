from fastapi import FastAPI
from app.schema import WeatherData
from app.predictor import predict

app = FastAPI(
    title="Rainfall Prediction API",
    version="1.0.0",
    description="Predict rainfall using a trained Linear Regression model."
)
