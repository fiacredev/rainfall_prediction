# 🌧️ Rainfall Prediction API

A clean, production-ready REST API that predicts **precipitation (in inches)** for a given day from weather measurements — powered by a scikit-learn machine learning pipeline and served with FastAPI.

## Features

-  **19 weather features** — temperature, dew point, humidity, sea-level pressure, visibility, wind and month
-  **Trained ML pipeline** — `StandardScaler` + `LinearRegression` serialized with Joblib
-  **Fast & async-ready** — built on FastAPI and Uvicorn
-  **Validated inputs** — Pydantic v2 guarantees well-formed request payloads
-  **Interactive docs** — Swagger UI and ReDoc out of the box
-  **Realistic output** — predictions clipped to the `0 – 5.2` inch range seen in training data

## Tech Stack

| Layer | Tool |
| --- | --- |
| Web framework | FastAPI |
| Server | Uvicorn |
| Validation | Pydantic v2 |
| ML | scikit-learn, pandas, NumPy, Joblib |
| Notebooks | Jupyter, matplotlib, seaborn |

## Project Structure

```
RainfallPredictionAPI/
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI app & routes
│   ├── predictor.py                # Model loading & prediction logic
│   └── schema.py                   # Pydantic request schema
├── models/
│   └── rainfall_pipeline.joblib    # Trained pipeline artifact
├── rainfall.ipynb                  # EDA & model training notebook
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`

### Installation

```bash
git clone https://github.com/fiacredev/RainfallPredictionAPI.git
cd RainfallPredictionAPI
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶ Running the API

```bash
uvicorn app.main:app --reload
```

Once running, the interactive documentation is available at:

- **Swagger UI** → http://127.0.0.1:8000/docs
- **ReDoc** → http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health check / welcome message |
| `POST` | `/predict` | Predict precipitation in inches |

### `GET /`

```json
{
  "message": "Rainfall Prediction API is running."
}
```

### `POST /predict`

Send the daily weather measurements — all 19 fields are required.

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "TempHighF": 85, "TempAvgF": 78, "TempLowF": 70,
    "DewPointHighF": 70, "DewPointAvgF": 64, "DewPointLowF": 58,
    "HumidityHighPercent": 85, "HumidityAvgPercent": 70, "HumidityLowPercent": 55,
    "SeaLevelPressureHighInches": 30.10, "SeaLevelPressureAvgInches": 30.02, "SeaLevelPressureLowInches": 29.94,
    "VisibilityHighMiles": 10, "VisibilityAvgMiles": 9, "VisibilityLowMiles": 7,
    "WindHighMPH": 15, "WindAvgMPH": 8, "WindGustMPH": 22,
    "Month": 5
  }'
```

**Response**

```json
{
  "predicted_precipitation_inches": 0.12
}
```

>  Predictions are clamped to the `[0, 5.2]` inch range observed in the training data, so the API never returns physically impossible values.

##  How the Model Works

1. **Data** — daily Austin weather history (`austin_weather.csv`).
2. **Cleaning** — the notebook replaces `-` placeholders with `0` and casts columns to numeric.
3. **Features** — 19 predictors: temperature, dew point, humidity, sea-level pressure, visibility, wind and month.
4. **Training** — a `StandardScaler` + `LinearRegression` pipeline is trained and evaluated in `rainfall.ipynb`.
5. **Deployment** — the fitted pipeline is exported to `models/rainfall_pipeline.joblib` and loaded once at API startup by `app/predictor.py`.

To retrain or explore the analysis:

```bash
jupyter notebook rainfall.ipynb
```

## Author

**Fiacre (fiacredev)**
✉️ fiacredeveloper@gmail.com
🐙 [github.com/fiacredev](https://github.com/fiacredev)

---
