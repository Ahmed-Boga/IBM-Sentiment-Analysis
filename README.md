# IBM Sentiment Analysis Using BERT

This repository contains a sentiment analysis project that uses IBM Watson's NLP API to classify text into positive, negative, or neutral sentiments. The application is built with Flask for backend services, HTML/JavaScript for the user interface, and Python for API integration and analysis.

---

## Project Structure

```graphql
graphql
Copy code
IBM-Sentiment-Analysis/
│
├── SentimentAnalysis/
│   ├── sentiment_analysis.py       # Core logic for sentiment analysis using IBM Watson API
│
├── templates/
│   ├── index.html                  # Frontend HTML interface for input and results
│
├── static/
│   ├── mywebscript.js              # JavaScript logic for frontend interactivity
│
├── server.py                       # Flask backend for handling API requests
├── test_sentiment_analysis.py      # Unit tests for sentiment analysis logic
└── README.md                       # Project documentation

```

---

## Features

1. **Sentiment Classification**
    
    Uses IBM Watson's BERT-based NLP API to classify text sentiment as:
    
    - Positive
    - Negative
    - Neutral
2. **Web Interface**
    
    A simple, interactive web interface to input text and view analysis results.
    
3. **Flask Backend**
    
    A lightweight Flask server handles user requests and communicates with the sentiment analysis API.
    
4. **Unit Testing**
    
    Validates the core sentiment analysis logic with pre-defined test cases.
    

---

## Prerequisites

- Python 3.7+
- Flask
- `requests` library
- Internet connection for accessing IBM Watson API

---

## Setup Instructions

1. **Clone the Repository**
    
    ```bash
    bash
    Copy code
    git clone https://github.com/your-repo/IBM-Sentiment-Analysis.git
    cd IBM-Sentiment-Analysis
    
    ```
    
2. **Install Dependencies**
    
    ```bash
    bash
    Copy code
    pip install flask requests
    
    ```
    
3. **Run the Application**
    
    ```bash
    bash
    Copy code
    python server.py
    
    ```
    
4. **Access the Web Interface**
Open a web browser and go to `http://127.0.0.1:5000`.

---

## API Details

### Sentiment Analysis Endpoint

- **URL**: `/sentimentAnalyzer`
- **Method**: `GET`
- **Query Parameter**:
    - `textToAnalyze`: Text input for sentiment analysis.
- **Response**:
    - Sentiment **label** (positive, negative, neutral).
    - Confidence **score**.

Example Request:

```perl
perl
Copy code
GET /sentimentAnalyzer?textToAnalyze=I%20love%20coding!

```

---

## Running Tests

Unit tests ensure that the sentiment analysis logic works correctly. Run tests with:

```bash
bash
Copy code
python -m unittest test_sentiment_analysis.py

```

---

## Example Output

### Input

> "I am excited to learn new skills!"
> 

### Output

```css
css
Copy code
{
  "label": "SENT_POSITIVE",
  "score": 0.92
}

```

The sentiment is identified as **positive** with a confidence score of `0.92`.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with your feature or bug fix.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **IBM Watson API**: Provides state-of-the-art sentiment analysis capabilities.
- **Flask**: Simplifies the development of the web application backend.
- **Bootstrap**: Powers the responsive and clean UI.

Happy Coding! 😊
