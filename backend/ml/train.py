import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

np.random.seed(42)
X = np.random.rand(10000, 2)
y = 3 * X[:, 0] + 5 * X[:, 1] + 2

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.joblib")

print("Model trained and saved")
