# Performance Analysis

## Objective

This document analyzes the throughput and latency characteristics of the ML Inference Service under concurrent load.  
The goal was to identify the dominant bottleneck in end-to-end request handling and evaluate whether inference optimization (Python vs ONNX vs C++) meaningfully impacts overall system performance.

---

## Test Environment

- Deployment: Docker (API + PostgreSQL)
- Backend: FastAPI + Uvicorn
- Database: PostgreSQL 15
- Inference modes: Python (sklearn), ONNX Runtime.
- Load testing tool: ApacheBench (ab)
- Host: Linux (local machine)
- Endpoint tested: POST /inferences
- Requests per test: 1000
- Concurrency level: 50
- Flag used: `-l` (to allow variable response length)

---

## Experimental Design

To isolate bottlenecks, two configurations were tested:

1. Inference + Database Write  
   - Performs model inference
   - Inserts result into PostgreSQL

2. Inference Only (_nodb mode)  
   - Performs model inference
   - Skips database insertion

All other variables were kept constant:
- Same payload
- Same concurrency
- Same containerized deployment

Additionally, PostgreSQL was tested with:
- `synchronous_commit = on` (default)
- `synchronous_commit = off` (experimental, non-production setting)

---

## Results

### ONNX + DB (Default: synchronous_commit = on)

- Concurrency: 50
- Requests/sec: ~320
- Mean latency: ~156 ms
- Total test time: ~3.1 seconds

### ONNX (No DB)

- Concurrency: 50
- Requests/sec: ~1087
- Mean latency: ~46 ms
- Total test time: ~0.92 seconds

### ONNX + DB (synchronous_commit = off)

- Concurrency: 50
- Requests/sec: ~511
- Throughput improvement: ~60% over default DB configuration

---

## Analysis

1. Database writes dominate end-to-end latency.
   Removing the database insert increased throughput by more than 3× and reduced mean latency significantly.

2. Inference optimization alone does not improve overall system throughput when synchronous database writes are enabled.

3. PostgreSQL durability guarantees (WAL flush + fsync) introduce measurable cost under concurrent write-heavy workloads.

4. Disabling `synchronous_commit` significantly improved throughput, confirming that disk flush operations were the primary bottleneck under load.

---

## Key Takeaways

- End-to-end system performance was I/O-bound, not CPU-bound.
- Micro-optimizing inference has limited effect when database commit latency dominates.
- There is a clear trade-off between durability guarantees and throughput.
- Performance bottlenecks must be identified at the system level, not at individual component level.

---

## Conclusion

This experiment demonstrates that in a containerized ML inference backend, database durability costs can outweigh inference computation costs under concurrent traffic.

Optimizing system performance requires identifying the true bottleneck — in this case, synchronous disk commits — rather than prematurely optimizing compute layers.
