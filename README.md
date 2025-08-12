## 📦 ML Deploy FastAPI

**Machine Learning Deployment using FastAPI and Uvicorn**  
Inspired by the ML Zoomcamp curriculum.

### 🚀 Overview

This project demonstrates how to deploy a machine learning model using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

It includes:
- A trained ML model (e.g., regression or classification)
- A FastAPI app for serving predictions
- Uvicorn as the ASGI server
- Docker support for containerized deployment

---

### 🧰 Tech Stack

- **FastAPI** – API framework
- **Uvicorn** – ASGI server
- **Scikit-learn / XGBoost / TensorFlow** – ML model (customizable)
- **Docker** – Containerization
- **Python 3.9+**

---

### 📁 Project Structure

```
ml-deploy-fastapi/
├── .github/                  # GitHub workflows or issue templates
├── .ipynb_checkpoints/       # Jupyter notebook checkpoints
├── .venv/                    # Python virtual environment
├── __pycache__/              # Compiled Python cache files
├── .dockerignore             # Docker ignore rules
├── .python-version           # Python version file (for pyenv)
├── Dockerfile                # Docker build instructions
├── fly.toml                  # Fly.io deployment config
├── main.py                   # FastAPI entry point
├── marketing.py              # Optional marketing-related logic
├── model.bin                 # Serialized ML model
├── model.py                  # Model loading and prediction logic
├── ping.py                   # Health check endpoint
├── predict.py                # Prediction endpoint
├── pyproject.toml            # Project metadata and dependencies
├── README.md                 # Project documentation
├── train.py                  # Model training script
├── uv.lock                   # Dependency lock file (for uv)
└── workshop-uv-fastapi.ipynb # Jupyter notebook for experimentation

### ⚙️ Setup & Run

#### 1. Install dependencies

```bash
pip install -r requirements.txt
```

#### 2. Run locally

```bash
uvicorn app.main:app --reload
```

#### 3. Build and run with Docker

```bash
docker build -t ml-deploy-fastapi .
docker run -p 8000:8000 ml-deploy-fastapi
```

---

### 📬 API Endpoint

- `POST /predict`  
  Send input features as JSON and receive model predictions.

Example:

```json


customer = {
  "gender": "male",
  "seniorcitizen": 0,
  "partner": "no",
  "dependents": "yes",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "yes",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "mailed_check",
  "tenure": 7,
  "monthlycharges": 29.75,
  "totalcharges": 131.9
}
```

---

### 📚 Credits

Based on the [ML Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code) course by Alexey Grigorev.
