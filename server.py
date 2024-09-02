"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the Flask app
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    This endpoint receives text from the HTML interface and
    runs sentiment analysis over it using the sentiment_analyzer()
    function. The output returned shows the label and its confidence
    score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided for analysis.", 400

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response.get('label')
    score = response.get('score')

    if label is None:
        return "Invalid input or analysis error. Please try again.", 500

    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as '{label.split('_')[1]}' with a score of {score}."

@app.route("/")
def render_index_page():
    """
    This function renders the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
