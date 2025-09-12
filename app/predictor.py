import joblib
import pandas as pd
from pathlib import Path

# Path to the saved pipeline
MODEL_PATH = Path(__file__).parent.parent / "models" / "rainfall_pipeline.joblib"

# Load once when the application starts
pipeline = joblib.load(MODEL_PATH)


def predict(data: dict):

    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)[0]

    prediction = max(0, min(prediction, 5.2))

    return float(prediction)
