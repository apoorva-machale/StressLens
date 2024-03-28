# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "I am feeling unwell and sad today"
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")

def sentiment_analysis_label(score, magnitude):
  sentiment_label = {
    "positive": {
      "score_range": (0.25, 1.0),
      "magnitude_range": (0.5, 1.0),
      "label": "Confident, Assertive"
    },
    "neutral": {
      "score_range": (-0.25, 0.25),
      "magnitude_range": (0.0, 1.0),
      "label": "Normal"
    },
    "negative": {
      "score_range": (-1.0, -0.25),
      "magnitude_range": (0.5, 1.0),
      "label": "Adverse sorrow"
    },
    "depression": {
      "score_range": (-1.0, -0.25),
      "magnitude_range": (0.0, 0.5),
      "label": "Feeling low"
    },
    "certain": {
      "score_range": (0.25, 1.0),
      "magnitude_range": (0.0, 0.5),
      "label": "Certain"
    }
  }

  for sentiment, criteria in sentiment_label.items():
    if (criteria["score_range"][0] <= score <= criteria["score_range"][1]) and (criteria["magnitude_range"][0] <= magnitude <= criteria["magnitude_range"][1]):
      return criteria["label"]
  
  # If no match is found, return 'Unknown'
  return "Unknown"

anaylsis = sentiment_analysis_label(sentiment.score, sentiment.magnitude)
print("Anaylsis:", anaylsis)
