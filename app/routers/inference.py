from fastapi import APIRouter, HTTPException
from schemas.inference import PredictionInput, PredictionResponse
from config.model import SentimentModel

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(input: PredictionInput):
    try:
        model = SentimentModel.get_model()
        prediction = model(input.text)
        return PredictionResponse(prediction=prediction[0]["label"])
    except Exception as error:
        print("Error on predict: ", error)
        raise HTTPException(status_code=500, detail="Internal server error")
