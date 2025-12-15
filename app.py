def analyze_sentiment_demo(text: str) -> str:
    positive_words = ["good", "great", "excellent", "amazing", "love", "awesome"]
    negative_words = ["bad", "terrible", "awful", "hate", "poor"]

    text_lower = text.lower()

    if any(word in text_lower for word in positive_words):
        return "positive"
    elif any(word in text_lower for word in negative_words):
        return "negative"
    else:
        return "neutral"


if __name__ == "__main__":
    user_text = input("Enter a sentence for sentiment analysis: ")
    sentiment = analyze_sentiment_demo(user_text)
    print(f"Sentiment: {sentiment} (demo mode)")
