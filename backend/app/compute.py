import numpy as np
# from app.cpp import cpp_inference

def python_compute(size: int):
    arr = np.random.rand(size)
    return (arr * arr).sum()

# def cpp_compute(size: int):
   # arr = np.random.rand(size)
   #  return cpp_inference.heavy_compute(arr)

