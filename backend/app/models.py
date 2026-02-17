from pydantic import BaseModel

class PredictRequest(BaseModel):
    x: float
    y: float
    mode: str

class PredictResponse(BaseModel):
    id : int
    x : float
    y : float
    result: float
