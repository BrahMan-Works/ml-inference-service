# ML Inference Service

A containerized, production-oriented ML inference backend built with FastAPI, PostgreSQL, and ONNX Runtime.

This project demonstrates clean RESTful API design, database integration, containerization, and inference acceleration using a C++-backed runtime engine.

---

## Features

- RESTful CRUD API for inference records
- PostgreSQL integration with connection pooling
- Automated database schema initialization
- Environment-based configuration (no hardcoded secrets)
- Global exception handling
- Dockerized deployment (API + DB)
- ONNX Runtime inference acceleration
- Load-tested and benchmarked

---

## Architecture

Client → FastAPI → Inference Engine (Sklearn / ONNX Runtime) → PostgreSQL

The service supports multiple inference modes:
- `python` (sklearn model)
- `onnx` (C++-backed ONNX runtime)

---

## API Endpoints

POST   /inferences  
GET    /inferences  
GET    /inferences/{id}  
DELETE /inferences/{id}

All responses use strict Pydantic validation.

---

## Running with Docker (Recommended)

From project root:

```bash
docker compose up --build
