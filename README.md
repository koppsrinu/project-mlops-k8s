Real-Time Price Prediction using SageMaker, Docker, Kubernetes & Streamlit
This project demonstrates a complete MLOps workflow, from model training on AWS SageMaker, to real-time inference with FastAPI on Kubernetes, and a beautiful UI using Streamlit.

🚀 Architecture
scss
Copy
Edit
User (via Streamlit UI)
        ↓
FastAPI Model API (K8s NodePort Service)
        ↓
XGBoost Model (Trained in SageMaker)
        ↓
Model Artifact from S3 → Served in K8s
📂 Project Structure
bash
Copy
Edit
.
├── train.py                # Model training script (XGBoost)
├── train.csv              # Sample training data
├── Dockerfile             # For training (BYOC SageMaker)
├── inference.py           # FastAPI serving script
├── app.py                 # Streamlit UI
├── deployment.yaml        # K8s deployment for model
├── service.yaml           # K8s service for model
├── deployment-ui.yaml     # K8s deployment for Streamlit
├── service-ui.yaml        # K8s service for Streamlit
└── README.md              # This file!
🔧 Tech Stack
Layer	Tool/Service
Model	XGBoost
Training	AWS SageMaker (BYOC with Docker)
Storage	Amazon S3
Inference	FastAPI
Serving	Kubernetes (Minikube or EKS)
UI	Streamlit
Container	Docker + Amazon ECR
📦 Setup Instructions
🧠 1. Train Your Model
Upload train.csv to S3

Build and push Docker image to ECR

Launch SageMaker training job using custom container

🐳 2. Inference API
Build & push FastAPI Docker image to ECR

Deploy using deployment.yaml + service.yaml

🌐 3. Streamlit UI
Build & push Streamlit UI image to ECR

Deploy using deployment-ui.yaml + service-ui.yaml

✅ Sample API Test
bash
Copy
Edit
curl -X POST http://<node-ip>:30036/predict \
  -H "Content-Type: application/json" \
  -d '{"feature1": 30000, "feature2": 10, "feature3": 0.85}'
📸 Streamlit Preview
🔥 UI with real-time predictions connected to live FastAPI + K8s model

![screenshot placeholder]

🙌 Author
Srinivas Koppolu
MLOps + DevOps Aspirant | Building end-to-end cloud AI pipelines
📍 India 🇮🇳 | AWS | Kubernetes | SageMaker | Streamlit
🔗 GitHub: koppsrinu

📘 License
MIT License — free to use, modify, deploy with your own data.
