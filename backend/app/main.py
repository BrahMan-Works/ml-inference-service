import logging

from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

@app.get("/health")
def health():
    return {"status": "ok"}
