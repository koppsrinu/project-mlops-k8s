FROM python:3.9-slim

WORKDIR /app

COPY model.joblib .
COPY inference.py .
RUN pip install fastapi uvicorn scikit-learn xgboost joblib numpy

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
