# High-Performance ML Inference Service

## Problem Statement
Python-based machine learning inference is easy to build and iterate on, but it often becomes a performance bottleneck in production systems. This project explores the performance tradeoffs between pure Python inference and optimized C++/CUDA-based inference, while retaining a Python backend for developer productivity.

The goal is to design and build a production-style ML inference service that is measurable, reproducible, and deployable on Linux.

---

## High-Level Architecture
The system is structured as a backend service that exposes machine learning inference through REST APIs. A Python-based FastAPI server handles request routing, validation, and orchestration. The ML inference layer initially uses a Python/PyTorch implementation as a baseline. Performance-critical inference components are then offloaded to a C++ (and optionally CUDA) implementation to evaluate latency and throughput improvements.

Metadata, request logs, and experiment results are stored in a PostgreSQL database. The entire system is designed to be containerized and reproducible using Docker.

---

## Tech Stack
- **Backend:** Python 3, FastAPI
- **Machine Learning:** PyTorch
- **Database:** PostgreSQL
- **Systems / Performance:** C++17 (optional CUDA)
- **Infrastructure:** Docker, Docker Compose
- **Platform:** Linux

---

## Planned Milestones
- **Week 1:** Linux environment setup, Git workflow, project scaffolding
- **Week 2:** REST API development with FastAPI and PostgreSQL integration
- **Week 3:** Database optimization, caching, and concurrency considerations
- **Week 4:** Dockerization, configuration management, and CI setup
- **Week 5–6:** ML model training and Python-based inference baseline
- **Week 7–8:** C++-based inference module and Python integration
- **Week 9–10:** Performance benchmarking and profiling
- **Week 11–12:** Documentation, cleanup and polish.
