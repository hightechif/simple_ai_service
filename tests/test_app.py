from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Simple AI Backend is running!"}

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this service, it is great!"})
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == "positive"
    assert data["score"] > 0

def test_predict_negative():
    response = client.post("/predict", json={"text": "This is terrible and bad."})
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == "negative"
    assert data["score"] < 0
