from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model.joblib")

# Input schema
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(X)
    return {"prediction": prediction[0]}
