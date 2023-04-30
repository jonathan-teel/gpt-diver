from flask import Flask, render_template, request, jsonify
import openai
import re
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/generate-analysis', methods=['POST'])
def generate_analysis():
    openai.api_key = request.form["api_key"]
    model = request.form['model']
    query = request.form['query']
    useSystem = request.form['sm']
    prompt = """Review the following input and provide the requested responses using the instructions provided for each response element. You should only respond with the JSON object with the specified format. "response" is the root JSON object. Make sure the JSON is parsable by json.loads(). You must ALWAYS respond with something in each response section. The JSON format as is follows:
    "response": {
        "answer": "Respond as you normally would as an AI chat bot",
        "analysis": "Provide an in-depth analysis of the query, discussing its context, relevance, and significance. Consider the possible implications and consequences of the query, as well as any underlying assumptions or biases",
        "interpretation": "Offer an interpretation of the query, focusing on the meanings, themes, or messages it conveys. Explore alternative interpretations and discuss any ambiguities, contradictions, or nuances present in the text",
        "emotional_analysis": "Analyze the emotional content of the query, identifying the emotions expressed or evoked by the text. Discuss how the choice of words, tone, and structure contribute to the emotional impact of the text, and provide examples to support your analysis",
        "suggestions": "Provide suggestions for improving, expanding, or refining the query. Consider aspects such as clarity, coherence, organization, and depth of the content. Offer specific recommendations for changes that could enhance the overall quality of the text",
        "thoughts": "Share your thoughts on the query, reflecting on the ideas, questions, or insights it raises. Consider the broader implications of the text, its relevance to current events or societal issues, and any personal connections or reactions you have to the content",
        "summarization": "Generate a concise summary, highlighting the key points and findings",
        "intent_detection": "Identify the intent behind the query, such as information-seeking, action-oriented, or social interaction, and provide suggestions for tailoring the response accordingly",
        "keywords_extraction": "Extract the most relevant keywords and phrases from the query, which can help users better understand the main focus and streamline the conversation",
        "sentiment_analysis": "Determine the sentiment (positive, negative, or neutral) expressed in the query, which can inform the tone and content of the response",
        "context_analysis": "Analyze the context in which the query was made, including any prior conversation, and consider that context when crafting a response",
        "anomaly_detection": "Detect any unusual patterns, inconsistencies, or contradictions in the query, and offer suggestions for addressing them in the response",
        "personalization": "Offer personalized response options based on the user's preferences, interaction history, or demographic information",
        "response_variations": "Generate multiple response options with varying levels of formality, detail, and tone, allowing users to choose the most suitable response for their needs"
    }
    Input: {input}"""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{'role': 'system', 'content': prompt}, {'role': 'user', 'content': query}] if useSystem else [{'role': 'user', 'content': prompt + query}]
        )
    except Exception as e:
        return jsonify({'error': str(e)})

    parsed_response = parse_response(response.choices[0].message.content.strip())
    answer = parsed_response['response']['answer']
    analysis = parsed_response['response']['analysis']
    interpretation = parsed_response['response']['interpretation']
    emotional_analysis = parsed_response['response']['emotional_analysis']
    suggestions = parsed_response['response']['suggestions']
    thoughts = parsed_response['response']['thoughts']
    summarization = parsed_response['response']['summarization']
    intent_detection = parsed_response['response']['intent_detection']
    keywords_extraction = parsed_response['response']['keywords_extraction']
    sentiment_analysis = parsed_response['response']['sentiment_analysis']
    context_analysis = parsed_response['response']['context_analysis']
    anomaly_detection = parsed_response['response']['anomaly_detection']
    personalization = parsed_response['response']['personalization']
    response_variations = parsed_response['response']['response_variations']

    return jsonify({'answer': answer, 'analysis': analysis, 'interpretation': interpretation, 'emotional_analysis': emotional_analysis, 'suggestions': suggestions
                    , 'thoughts': thoughts, 'summarization': summarization, 'intent_detection': intent_detection, 'keywords_extraction': keywords_extraction
                    , 'sentiment_analysis': sentiment_analysis, 'context_analysis': context_analysis, 'anomaly_detection': anomaly_detection
                    , 'personalization': personalization, 'response_variations': response_variations})

def parse_response(message):
    json_start = re.search(r'\{', message).start()
    ret = message[json_start:]
    try:
        j = json.loads(ret)
    except json.JSONDecodeError as e:
        j = None
        print(f"JSONDecodeError: {e}")
        print(f"For Value: {message}")
    return j

if __name__ == '__main__':
    app.run(debug=True)