from fastapi import APIRouter, HTTPException
from .models import PredictRequest, PredictResponse
from .db import get_connection

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = req.x + req.y

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO inference_requests (x, y, result)
        VALUES (%s, %s, %s)
        RETURNING id;
        """,
        (req.x, req.y, result)
    )

    inserted_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return PredictResponse(
        id=inserted_id,
        x=req.x,
        y=req.y,
        result=result
    )


@router.get("/predict/{request_id}", response_model=PredictResponse)
def get_prediction(request_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, x, y, result
        FROM inference_requests
        WHERE id = %s;
        """,
        (request_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Prediction Not Found")

    return PredictResponse(
        id=row[0],
        x=row[1],
        y=row[2],
        result=row[3]
    )

