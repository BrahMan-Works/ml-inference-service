import uuid
import logging
import numpy as np
import app.model_loader as model_loader

from fastapi import APIRouter, HTTPException
from app.models import PredictRequest, PredictResponse
from app.repository import insert_inference, get_inference_by_id

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Incoming /predict request: x={req.x}, y={req.y}")

    if model_loader.model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    input_data = np.array([[req.x, req.y]])
    result = float(model_loader.model.predict(input_data)[0])

    try:
        inference_id = insert_inference(req.x, req.y, result)
        logging.info(f"[{request_id}] DB insert successful, id={inference_id}")
    except Exception as e:
        logging.error(f"[{request_id}] DB insert failed: {e}")
        raise HTTPException(status_code=500, detail="Database error")

    return PredictResponse(id=inference_id, x=req.x, y=req.y, result=result)


@router.get("/predict/{inference_id}")
def get_prediction(inference_id: int):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Fetching inference id={inference_id}")

    row = get_inference_by_id(inference_id)

    if row is None:
        logging.warning(f"[{request_id}] Inference id={inference_id} not found")
        raise HTTPException(status_code=404, detail="Inference not found")

    logging.info(f"[{request_id}] Inference id={inference_id} found")

    return {
        "id": row[0],
        "x": row[1],
        "y": row[2],
        "result": row[3],
    }

