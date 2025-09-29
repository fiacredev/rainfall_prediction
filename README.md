# 🌧️ Rainfall Prediction API

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=flat-square&logo=fastapi&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.9.0-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

A clean, production-ready REST API that predicts **precipitation (in inches)** for a given day from weather measurements — powered by a scikit-learn machine learning pipeline and served with FastAPI.

## ✨ Features

- 🌡️ **19 weather features** — temperature, dew point, humidity, sea-level pressure, visibility, wind and month
- 🤖 **Trained ML pipeline** — `StandardScaler` + `LinearRegression` serialized with Joblib
- ⚡ **Fast & async-ready** — built on FastAPI and Uvicorn
- ✅ **Validated inputs** — Pydantic v2 guarantees well-formed request payloads
- 📖 **Interactive docs** — Swagger UI and ReDoc out of the box
- 🎯 **Realistic output** — predictions clipped to the `0 – 5.2` inch range seen in training data

## 🛠️ Tech Stack

| Layer | Tool |
| --- | --- |
| Web framework | FastAPI |
| Server | Uvicorn |
| Validation | Pydantic v2 |
| ML | scikit-learn, pandas, NumPy, Joblib |
| Notebooks | Jupyter, matplotlib, seaborn |

## 📂 Project Structure

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

## 🚀 Getting Started

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

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
```

Once running, the interactive documentation is available at:

- **Swagger UI** → http://127.0.0.1:8000/docs
- **ReDoc** → http://127.0.0.1:8000/redoc
