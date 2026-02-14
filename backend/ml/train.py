import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

np.random.seed(42)

X = np.random.rand(20000, 50)
y = X.sum(axis=1) * 2 + np.random.randn(20000) * 0.1

model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            n_jobs=-1
        )

model.fit(X, y)

joblib.dump(model, "model.joblib")

print("Model trained and saved")
