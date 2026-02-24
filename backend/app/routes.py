import uuid
import logging
import numpy as np
import app.model_loader as model_loader

from typing import List
from fastapi import APIRouter, HTTPException, status
from app.models import InferenceCreateRequest, InferenceResponse
from app.compute import python_compute, cpp_compute
from app.repository import insert_inference, get_inference_by_id, delete_inference_by_id, list_inferences_from_db
from app.onnx_loader import onnx_predict

router = APIRouter()

@router.post("/inferences", status_code=201, response_model=InferenceResponse)
def create_inference(req: InferenceCreateRequest):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Incoming /predict request")

    if model_loader.model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    features = np.random.rand(1, 50)
    mode = req.mode

    if mode == "python":
        result = float(model_loader.model.predict(features)[0])
    elif mode == "onnx":
        result = float(onnx_predict(features)[0][0])
    else:
        raise HTTPException(status_code=400, detail="Invalid mode")

    try:
        inference_id = insert_inference(req.x, req.y, result)
        logging.info(f"[{request_id}] DB insert successful, id={inference_id}")
    except Exception as e:
        logging.error(f"[{request_id}] DB insert failed: {e}")
        raise HTTPException(status_code=500, detail="Database error")

    return InferenceResponse(id=inference_id, x=req.x, y=req.y, result=result)


@router.get("/inferences", response_model=List[InferenceResponse])
def list_inferences():
    records = list_inferences_from_db()
    return records


@router.get("/inferences/{inference_id}", response_model=InferenceResponse)
def get_inference(inference_id: int):
    request_id = str(uuid.uuid4())
    logging.info(f"[{request_id}] Fetching inference id={inference_id}")

    row = get_inference_by_id(inference_id)

    if row is None:
        logging.warning(f"[{request_id}] Inference id={inference_id} not found")
        raise HTTPException(status_code=404, detail="Inference not found")

    logging.info(f"[{request_id}] Inference id={inference_id} found")

    return InferenceResponse(
        id = row[0],
        x = row[1],
        y = row[2],
        result = row[3],
    )


@router.delete("/inferences/{inference_id}", status_code=204)
def delete_inference(inference_id: int):
    deleted = delete_inference_by_id(inference_id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inference not found")

    return
