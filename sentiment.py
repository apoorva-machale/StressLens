# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()


def sentiment_analysis_label(text):
  result = {}
  document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
  )
  
  # Detects the sentiment of the text
  sentiments = client.analyze_sentiment(
    request={"document": document}
  ).document_sentiment

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
    if (criteria["score_range"][0] <= sentiments.score <= criteria["score_range"][1]) and (criteria["magnitude_range"][0] <= sentiments.magnitude <= criteria["magnitude_range"][1]):
      result['sentiment_score'] = sentiments.score
      result['sentiment_magnitude'] = sentiments.magnitude
      result['analysis'] = criteria["label"]
      # print("result", result)
      return result
  
  # If no match is found, return 'Unknown'
  return "Unknown"

# text = "I am sad today because I was not able to focus on my studies today"
# analysis = sentiment_analysis_label(text)
# print(analysis)

