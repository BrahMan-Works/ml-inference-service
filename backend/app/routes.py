from fastapi import APIRouter
from .models import PredictRequest, PredictResponse

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return PredictResponse(result=req.x + req.y)
