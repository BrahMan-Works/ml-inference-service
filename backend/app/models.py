from pydantic import BaseModel
from typing import Optional

class InferenceCreateRequest(BaseModel):
    x: float
    y: float
    mode: str

class InferenceResponse(BaseModel):
    id : int
    x : float
    y : float
    result: float
