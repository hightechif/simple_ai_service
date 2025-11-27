# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from .ai_model import analyze_sentiment

app = FastAPI(
    title="Simple AI Service",
    description="A lightweight FastAPI backend with AI functionality",
    version="1.0"
)

# Request body schema
class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Simple AI Backend is running!"}

@app.post("/predict")
def predict(req: TextRequest):
    result = analyze_sentiment(req.text)
    return {
        "input": req.text,
        "prediction": result["sentiment"],
        "score": result["score"]
    }
