from pydantic import BaseModel

class WeatherData(BaseModel):
    TempHighF: float
    TempAvgF: float
    TempLowF: float
    DewPointHighF: float
    DewPointAvgF: float
    DewPointLowF: float
