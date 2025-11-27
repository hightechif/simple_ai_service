# ai_model.py

positive_words = ["good", "great", "love", "awesome", "happy", "excellent"]
negative_words = ["bad", "sad", "terrible", "hate", "awful", "poor"]

def analyze_sentiment(text: str) -> dict:
    text_lower = text.lower()

    score = 0
    for w in positive_words:
        if w in text_lower:
            score += 1
    for w in negative_words:
        if w in text_lower:
            score -= 1

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
