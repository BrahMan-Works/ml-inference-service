import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import router
from app.db import init_connection_pool
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
    logging.info("Starting application...")

    init_connection_pool()
    logging.info("Database connection pool initialized.")

    load_model()
    logging.info("Sklearn model loaded.")

    load_onnx_model()
    logging.info("ONNX model loaded.")


@app.get("/health")
def health():
    return {"status": "ok"}
