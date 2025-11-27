# Simple AI Service

A FastAPI-based backend for text sentiment analysis, containerized with Docker and deployed on Google Cloud Run.

## 🚀 Live Demo

The service is currently up and running on Google Cloud Platform.

- **Base URL:** `https://simple-ai-service-ahwjz2njsa-uc.a.run.app`
- **Interactive Docs (Swagger UI):** [Click here to view docs](https://simple-ai-service-ahwjz2njsa-uc.a.run.app/docs)

## ⚡ API Usage

### 1. Health Check
Check if the service is running.

```bash
curl https://simple-ai-service-ahwjz2njsa-uc.a.run.app/
```

### 2. Sentiment Analysis
Send a POST request to analyze text.

```bash
curl -X POST "https://simple-ai-service-ahwjz2njsa-uc.a.run.app/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I really love this product, it is awesome!"}'
```
---

## 🛠️ Local Development
### Requirements
- [Docker](https://www.docker.com/)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Quick Start
1. **Install dependencies:**
```bash
uv sync
```

2. **Activate virtual environment:**
```bash
source .venv/bin/activate
```

3. **Run the server locally:**
```bash
fastapi run app/main.py
```

### Docker Development

You can simulate the production environment locally using the Dockerfile.

**Build the image:**
```bash
docker build -t simple-ai-app .
```

**Run the container:**
```bash
# We use PORT 8080 to simulate the Cloud Run environment
docker run -e PORT=8080 -p 8080:8080 simple-ai-app
```
---
## ☁️ Deployment (Google Cloud Run)

This project is deployed using Google Artifact Registry and Cloud Run.

1. **Build & Push Image**
Note: Replace [YOUR_PROJECT_ID] with your GCP Project ID.

```bash
# Build for Linux AMD64 (required for Cloud Run)
docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/[YOUR_PROJECT_ID]/simple-ai-repo/simple-ai-app:v2 .

# Push to Artifact Registry
docker push us-central1-docker.pkg.dev/[YOUR_PROJECT_ID]/simple-ai-repo/simple-ai-app:v2
```

2. **Deploy to Cloud Run**
```bash
gcloud run deploy simple-ai-service \
    --image us-central1-docker.pkg.dev/[YOUR_PROJECT_ID]/simple-ai-repo/simple-ai-app:v2 \
    --region us-central1 \
    --allow-unauthenticated
```
---
## 📂 Project Structure
- `app/main.py`: Entry point for the application.
- `app/ai_model.py`: Simple AI model for text sentiment analysis.
- `Dockerfile`: Configuration for building the production container (optimized for uv & Cloud Run).

## 🧪 Testing
To run the backend tests:
```bash
bash ./scripts/test.sh
```

Tests are run using Pytest. You can see coverage reports in `htmlcov/index.html`.
