import joblib
import pandas as pd
from pathlib import Path

# Path to the saved pipeline
MODEL_PATH = Path(__file__).parent.parent / "models" / "rainfall_pipeline.joblib"

# Load once when the application starts
pipeline = joblib.load(MODEL_PATH)
