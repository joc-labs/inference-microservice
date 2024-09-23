from transformers import pipeline
from constants.main import MODEL_NAME


class SentimentModel:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = pipeline(
                "sentiment-analysis", model=MODEL_NAME)
        return cls._model
