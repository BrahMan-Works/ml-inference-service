import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import router
from app.model_loader import load_model
from app.onnx_loader import load_onnx_model

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

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
