import logging

from fastapi import FastAPI
from app.routes import router
from app.model_loader import load_model
from app.onnx_loader import load_onnx_model

app = FastAPI()
app.include_router(router)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

@app.on_event("startup")
def startup():
    load_onnx_model()

@app.on_event("startup")
def startup_event():
    load_model()
    logging.info("Model loaded")

@app.get("/health")
def health():
    return {"status": "ok"}
