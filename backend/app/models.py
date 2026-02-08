from pydantic import BaseModel

class PredictRequest(BaseModel):
    x: float
    y: float

class PredictResponse(BaseModel):
    result: float
