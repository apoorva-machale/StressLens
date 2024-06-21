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

  sentiment_label = [
    {
      "score_range": (0.25, 1.0),
      "magnitude_range": (0.5, 1.0),
      "label": "Confident, Assertive"
    },
    {
      "score_range": (0.25, 1.0),
      "magnitude_range": (0.0, 0.5),
      "label": "Certain, Positive"
    },
    {
      "score_range": (-0.25, 0.25),
      "magnitude_range": (0.0, 1.0),
      "label": "Normal"
    },
    {
      "score_range": (-1.0, -0.25),
      "magnitude_range": (0.5, 1.0),
      "label": "Adverse sorrow"
    },
    {
      "score_range": (-1.0, -0.25),
      "magnitude_range": (0.0, 0.5),
      "label": "Feeling low"
    },
  ]
  # print("Hi")
  # print("sentiments",sentiments)
  # print("sentiments type",type(sentiments))
  if not sentiments.score:
    sentiments.score = 0
  if not sentiments.magnitude:
    sentiments.magnitude = 0
  for sentiment in sentiment_label:
    if (sentiment["score_range"][0] <= sentiments.score <= sentiment["score_range"][1]) and (sentiment["magnitude_range"][0] <= sentiments.magnitude <= sentiment["magnitude_range"][1]):
      result['sentiment_score'] = sentiments.score
      result['sentiment_magnitude'] = sentiments.magnitude
      result['analysis'] = sentiment["label"]
      print("result", result)
      return result
  result['sentiment_score'] = sentiments.score
  result['sentiment_magnitude'] = sentiments.magnitude
  result['analysis'] = "Unknown behaviour"
  # If no match is found, return 'Unknown'
  return result

# text = "I am sad today because I was not able to focus on my studies today"
# analysis = sentiment_analysis_label(text)
# print(analysis)

