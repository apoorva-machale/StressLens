from google.cloud import language_v1

# text_content = "In Fullerton right now, it's a cool 58 degrees Fahrenheit and cloudy. There's a chance of showers throughout the day, with a high expected to only reach 58 degrees and a low of 48 degrees Fahrenheit.  The wind is blowing moderately from the south at 9 mph."
def classify_text(text_content):
    output = []
    #check if the text_content has atleast 20 words and then only proceed or return can't classify due to short words
    word_count = len(text_content.split())
    if word_count < 25:
        return "Insufficient word count"
    
    client = language_v1.LanguageServiceClient()

    # text_content = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
    )
    response = client.classify_text(
        request={
            "document": document,
            "classification_model_options": {
                "v2_model": {"content_categories_version": content_categories_version}
            },
        }
    )
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(f"Category name: {category.name}")
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(f"Confidence: {category.confidence}")
        current_classification = {}
        current_classification['category_name'] = category.name
        current_classification['category_confidence'] = category.confidence
        output.append(current_classification)
    
    return output



