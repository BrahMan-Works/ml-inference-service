from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "inference_requests_total",
    "Total inference requests",
    ["backend"]
)

REQUEST_LATENCY = Histogram(
    "inference_latency_seconds",
    "Latency of inference requests",
    ["backend"]
)

