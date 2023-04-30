# GPT-Diver

GPT-Diver is a Flask web application that provides an interface for users to interact with OpenAI's GPT model. Users can submit a query and receive various types of analysis and response options based on the query, which can help improve the user's understanding of the model's behavior. The query can be reran with a selected responsed attached as query history. The following responses are received:

 "response": {
	"answer"
	"analysis"
	"interpretation"
	"emotional_analysis"
	"suggestions"
	"thoughts"
	"summarization"
	"intent_detection"
	"keywords_extraction"
	"sentiment_analysis"
	"context_analysis"
	"anomaly_detection"
	"personalization"
	"response_variations"
}

## Features

- Analyze and inspect different aspects of GPT's response to a given query
- Resubmit queries with additional context or modified prompts
- Explore various AI techniques and their application to user queries

## Installation

1. Clone the repository:
git clone https://github.com/jonathan-teel/gpt-dive.git
cd gpt-dive

2. Install the required packages:
pip install -r requirements.txt

## Usage

1. Run the Flask application:
python app.py

2. Open your browser and navigate to http://127.0.0.1:5000/.

3. Enter your query in the input field and click the "Run" button. The application will display GPT's response along with several other insights, such as emotional analysis, summarization, and more.

4. You can resubmit your query with any of the provided insights.

## Contributing

Contributions are welcome, please feel free to submit a pull request or create an issue for any bugs or feature requests.

## License

GPT-Diver is released under the MIT License - see the LICENSE for details.