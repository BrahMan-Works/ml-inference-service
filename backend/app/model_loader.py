import joblib
import os

model = None

def load_model():
    global model
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir ,"..", "ml", "model.joblib")
    model_path = os.path.abspath(model_path)

    model = joblib.load(model_path)
