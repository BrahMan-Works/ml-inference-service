import numpy as np
from app.ml_model import predict as torch_predict
from app.cpp import cpp_inference

def python_compute(features):
    return float(np.sum(features))

def torch_compute(features):
    result = torch_predict(features)
    return float(result[0][0])

def cpp_compute(size: int):
    arr = np.random.rand(size)
    return cpp_inference.heavy_compute(arr)   

