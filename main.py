from flask import Flask, render_template, request, jsonify
import openai
import re
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/generate-analysis', methods=['POST'])
def generate_analysis():
    openai.api_key = request.form["api_key"]
    model = request.form['model']
    query = request.form['query']
    useSystem = request.form['sm']
    temperature = float(request.form['temperature'])
    top_p = float(request.form['top_p'])
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
            temperature=temperature,
            top_p=top_p,
            messages=[{'role': 'system', 'content': prompt}, {'role': 'user', 'content': query}] if useSystem else [{'role': 'user', 'content': prompt + query}]
        )
    except Exception as e:
        return jsonify({'error': str(e)})

    parsed_response = parse_response(response.choices[0].message.content.strip())
    if(parsed_response == 'error'):
        return jsonify({'error': 'BAD_PARSE', 'result': response.choices[0].message.content.strip()})
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

@app.route('/generate-patois', methods=['POST'])
def generate_patois():
    openai.api_key = request.form["api_key"]
    model = request.form['model']
    query = request.form['query']
    gpt_patois_format_definition = """
    Full Formal Specification:
    1. General Structure

    A typical GPT-Patois control block looks like this:

    BLOCK_TYPE {
        Parameter1: "Value",
        Parameter2: "Value",
        ...
    }

    There is not parent block.

    The following sections outline each block type, its purpose, and the possible parameters it may contain.

    2.1 Conversation Block (CB)
    This block sets the overall context for the conversation. It includes the parameters for Personality, Topic, Focus, Detail, Characters, and Event.

    2.2 Role Block (RB)
    This block defines the role the AI should take in the conversation, with parameters such as Role to define the assistant's role.

    2.3 Prompt Block (PB)
    This block contains the user's prompt or command, including the parameter Prompt which holds the user's question or instruction.

    2.4 Emotion Block (EB)
    The block sets the emotional tone for the AI's responses, containing the Emotion parameter to set the emotional tone of the assistant.

    2.5 Knowledge Block (KB)
    This block specifies the domain of knowledge from which the assistant should draw. It contains the Domain parameter which sets the knowledge domain.

    2.6 Time Block (TB)
    This block sets a temporal context for the assistant's responses, with a Time parameter to define a specific time or time period.

    2.7 Location Block (LB)
    This block sets a location context for the AI's responses, containing a Location parameter to set a specific geographical context.

    2.8 Factuality Block (FB)
    This block controls the level of factual accuracy in the assistant's responses, with Factuality as its parameter to set the level of factual accuracy.

    2.9 Style Block (SB)
    This block controls stylistic aspects of the assistant's responses, with Style and Verbosity as its parameters.

    2.10 Detail Level Block (DLB)
    This block controls the level of detail in the assistant's responses, with Detail as its parameter to control the level of detail in the assistant's responses.

    2.11 Language Block (LangB)
    This block sets the language of the assistant's responses, containing Language as its parameter.

    2.12 Bias Control Block (BCB)
    This block allows controlling any potential bias in the assistant's responses, with Bias as its parameter.

    2.13 Genre Block (GB)
    This block sets a specific genre for story generation or other creative writing tasks, containing Genre as its parameter.

    2.14 Sensory Detail Block (SDB)
    This block sets the level of sensory detail in the assistant's responses, containing SensoryDetail as its parameter.

    2.15 Imagination Block (IB)
    This block controls the level of imagination and creativity in the assistant's responses, with Imagination as its parameter.

    2.16 Fact Check Block (FCB)
    This block instructs the assistant to fact-check a piece of information, containing Fact as its parameter.

    2.17 Temporal Control Block (TCB)
    This block sets a time context for the assistant's responses, containing Time as its parameter to specify a time period.

    2.18 Contextual Block (CtxB)
    This block provides detailed contextual information for the AI's responses, containing CurrentEvent as its parameter.

    2.19 Sociolinguistic Block (SLB)
    This block influences the politeness level, formality, or dialect in responses, containing Politeness as its parameter.

    2.20 Sentiment Analysis Block (SAB)
    This block influences the overall sentiment of the model's responses, containing Sentiment as its parameter.

    2.21 Interactive Block (IB)
    This block generates interactive elements in the conversation, containing InteractiveElement as its parameter.


    3. Nesting Feature

    The nesting feature allows users to nest multiple blocks within each other to create complex sub-contexts. This offers more nuanced control over AI responses.

    A typical nesting syntax looks like this:

    BLOCK_TYPE {
        Parameter1: "Value",
        BLOCK_TYPE {
            Parameter1: "Value",
            Parameter2: "Value",
            ...
        },
        Parameter2: "Value",
        ...
    }

    To explain further, let's take a practical example:

    PB {
        Prompt: "Describe the social and economic changes that occurred during the Industrial Revolution."
    }
    CB {
        Personality: "historian",
        Topic: "history",
        RB {
            Role: "Teacher"
        },
        Focus: "industrial revolution",
    }

    In this example, a Role Block (RB) is nested inside a Conversation Block (CB). This means that within the conversation context defined by the Conversation Block, the assistant takes on a specific role as defined by the nested Role Block.

    The nesting feature adds another dimension to the specificity and complexity of instructions you can give to the AI model.

    Compile the following input into strict GPT-Patois format, adding as many blocks as possible. Input:\n
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{'role': 'user', 'content': gpt_patois_format_definition + query}]
        )
    except Exception as e:
        return jsonify({'error': str(e)})

    return jsonify({'answer': response.choices[0].message.content.strip()})

def parse_response(message):
    json_start = re.search(r'\{', message).start()
    ret = message[json_start:]
    try:
        return json.loads(ret)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(f"For Value: {message}")
        return 'error'

if __name__ == '__main__':
    app.run()