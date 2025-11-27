# ai_model.py
from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    blob = TextBlob(text)
    score = blob.sentiment.polarity

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment,
        "score": score
    }
