import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from joblib import dump
import os

# SageMaker input data path
input_path = "/opt/ml/input/data/train/train.csv"

# Read training data from the S3-mounted input path
data = pd.read_csv(input_path)
X = data.drop("target", axis=1)
y = data["target"]

# Train model
model = xgb.XGBRegressor()
model.fit(X, y)

# Save the model in the required SageMaker directory
model_dir = "/opt/ml/model"
os.makedirs(model_dir, exist_ok=True)
dump(model, os.path.join(model_dir, "model.joblib"))

print("✅ Model trained and saved to /opt/ml/model/model.joblib")
