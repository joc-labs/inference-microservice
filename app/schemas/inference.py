from pydantic import BaseModel


class PredictionInput(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    prediction: str
