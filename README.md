# GPU-Accelerated ML Inference Service

A high-performance machine learning inference API built with **FastAPI**, **CUDA**, and **PyTorch**, designed to simulate a production-style ML inference system with **GPU acceleration, async request handling, benchmarking, and observability**.

The project explores how different inference backends perform under load while running inside a fully containerized environment.

---

## 🚀 Key Features

* GPU-accelerated inference using **PyTorch + CUDA**
* **ONNX Runtime** inference for performance comparison
* **FastAPI async API** for high concurrency
* **Dynamic batching experiments** for GPU throughput
* **PostgreSQL logging** with async writes
* **Dockerized CUDA environment**
* **Prometheus metrics instrumentation**
* **ApacheBench load testing**
* Throughput benchmarking across concurrency levels

---

## 🧠 System Architecture

```
Client
   │
   ▼
FastAPI Inference API
   │
   ├── GPU Inference
   │     ├── PyTorch (CUDA)
   │     ├── ONNX Runtime
   │     └── Python baseline
   │
   ├── Async Write Queue
   │
   ▼
PostgreSQL Database

Metrics → Prometheus
```

---

## 📊 Observability

The service exposes Prometheus metrics:

```
/metrics
```

Key metrics include:

* `inference_requests_total`
* `inference_latency_seconds`
* `gpu_inference_seconds`

This allows monitoring of:

* request throughput
* latency distribution
* GPU compute time

---

## 🧪 Benchmarking

Load testing performed using **ApacheBench**.

Example benchmark:

```
ab -l -n 5000 -c 100 \
-T application/json \
-p payload.json \
http://localhost:8000/inferences_async
```

## ⚡ Performance Benchmark

Throughput measured using **ApacheBench** across increasing concurrency levels.

| Concurrency | Requests/sec |
| ----------- | ------------ |
| 25          | ~854         |
| 50          | ~919         |
| 100         | ~924         |
| 200         | ~926         |

The system saturates around **~920 requests/sec**, demonstrating the concurrency ceiling of the current architecture.


---

## 🖥 GPU Acceleration

Inference runs on GPU using:

* **PyTorch CUDA**
* **mixed precision (Tensor Cores)**
* **batched inference**

Example model:

```
ResNet18
```

The system uses batching to better utilize GPU compute resources.

---

## 🐳 Running the Project

### Start services

```
docker compose up --build
```

Services started:

* API server
* PostgreSQL database

---

### Access API

```
http://localhost:8000/docs
```

Metrics endpoint:

```
http://localhost:8000/metrics/
```

---

## 🧰 Tech Stack

* Python
* FastAPI
* PyTorch
* ONNX Runtime
* CUDA
* PostgreSQL
* Docker
* Prometheus
* ApacheBench

---

## 📄 License

MIT License
