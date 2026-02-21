import os
import onnxruntime as ort
import numpy as np
import logging

session = None
input_name = None

def load_onnx_model():
    global session, input_name
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "../ml/model.onnx")
    model_path = os.path.abspath(model_path)

    session = ort.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
    
    logging.info("ONNX model loaded.")

def onnx_predict(features: np.ndarray):
    outputs = session.run(None, {input_name: features.astype(np.float32)})
    return outputs[0]
