# Deployment Guide - Google Cloud Run

This guide will help you deploy your Simple AI Service to Google Cloud Run.

## Prerequisites

1.  **Google Cloud Project**: You need a GCP project.
2.  **Billing Enabled**: Ensure billing is enabled for your project.
3.  **Google Cloud SDK**: Ensure `gcloud` CLI is installed and configured.

## Deployment Steps

### 1. Enable Required APIs

Run the following command to enable Cloud Build and Cloud Run APIs:

```bash
gcloud services enable cloudbuild.googleapis.com run.googleapis.com
```

### 2. Build and Deploy

You can build the container and deploy it in a single step using `gcloud run deploy`. This command uploads your source code, builds the container using Cloud Build, and deploys it to Cloud Run.

Run the following command from the root of your project:

```bash
gcloud run deploy simple-ai-service \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

- `simple-ai-service`: The name of your Cloud Run service.
- `--source .`: Builds the container from the current directory.
- `--platform managed`: Uses the fully managed Cloud Run platform.
- `--region us-central1`: Deploys to the US Central 1 region (you can change this).
- `--allow-unauthenticated`: Makes the service publicly accessible. Remove this flag if you want to restrict access.

### 3. Verify Deployment

After the deployment finishes, `gcloud` will output a Service URL (e.g., `https://simple-ai-service-xyz-uc.a.run.app`).

You can test it using `curl`:

```bash
curl https://YOUR_SERVICE_URL/
```

And test the prediction endpoint:

```bash
curl -X POST https://YOUR_SERVICE_URL/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Cloud Run is amazing!"}'
```
