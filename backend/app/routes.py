import uuid
import logging
import numpy as np
import app.model_loader as model_loader

from fastapi import APIRouter, HTTPException
from app.models import PredictRequest, PredictResponse
from app.compute import python_compute, cpp_compute
# from app.repository import insert_inference, get_inference_by_id

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Incoming /predict request")

    if model_loader.model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    features = np.random.rand(5_000_000)
    # result = float(model_loader.model.predict(features)[0])

    # try:
        # inference_id = insert_inference(req.x, req.y, result)
        # logging.info(f"[{request_id}] DB insert successful, id={inference_id}")
    # except Exception as e:
        # logging.error(f"[{request_id}] DB insert failed: {e}")
        # raise HTTPException(status_code=500, detail="Database error")

    size = 10_000_000
    mode = req.mode;

    if mode == "python":
        result = python_compute(size)
    elif mode == "cpp":
        result = cpp_compute(size)
    else:
        raise HTTPException(status_code=400, detail="Invalid mode")

    return PredictResponse(id=1, x=req.x, y=req.y, result=result)


@router.get("/predict/{inference_id}")
def get_prediction(inference_id: int):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Fetching inference id={inference_id}")

    # row = get_inference_by_id(inference_id)

    if row is None:
        logging.warning(f"[{request_id}] Inference id={inference_id} not found")
        raise HTTPException(status_code=404, detail="Inference not found")

    logging.info(f"[{request_id}] Inference id={inference_id} found")

    return {
        "id": 1,
        "x": 0,
        "y": 0,
        "result": 0,
    }

