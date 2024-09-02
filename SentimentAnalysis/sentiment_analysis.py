import requests
import json

def sentiment_analyzer(text_to_analyse):
    """
    Sends a request to the sentiment analysis API with the given text.
    Returns the sentiment label and score.
    """
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    payload = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        formatted_response = response.json()

        # Extract the label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {'label': None, 'score': None}
    except Exception as err:
        print(f"Other error occurred: {err}")
        return {'label': None, 'score': None}

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
