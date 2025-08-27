from pydantic import BaseModel

class WeatherData(BaseModel):
    TempHighF: float
    TempAvgF: float
    TempLowF: float
    DewPointHighF: float
    DewPointAvgF: float
    DewPointLowF: float
    HumidityHighPercent: float
    HumidityAvgPercent: float
    HumidityLowPercent: float
