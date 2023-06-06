document.addEventListener('DOMContentLoaded', () => {
    var answer = document.getElementById('answer');
    var analysis = document.getElementById('analysis');
    var interpretation = document.getElementById('interpretation');
    var emotionalAnalysis = document.getElementById('emotional-analysis');
    var suggestions = document.getElementById('suggestions');
    var thoughts = document.getElementById('thoughts');
    var summarization = document.getElementById('summarization');
    var intentDetection = document.getElementById('intent-detection');
    var keywordsExtraction = document.getElementById('keywords-extraction');
    var sentimentAnalysis = document.getElementById('sentiment-analysis');
    var contextAnalysis = document.getElementById('context-analysis');
    var anomalyDetection = document.getElementById('anomaly-detection');
    var personalization = document.getElementById('personalization');
    var responseVariations = document.getElementById('response-variations');
    var runBtn = document.getElementById('runBtn');
    var patoisBtn = document.getElementById('patoisBtn');
    var thoughtsSpinner = document.getElementById('thoughts-spinner');
    thoughtsSpinner.style.display = 'none';
    var originalQuery = '';
    var queryHistory = '';

    runBtn.addEventListener('click', async (event) => {
        originalQuery = document.getElementById('query').value;
        queryHistory = '';
        generateAnalysis();
    });

    patoisBtn.addEventListener('click', async (event) => {
        generateGptPatois()
    });

    document.getElementById('runAnswerBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${answer.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runAnalysisBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${analysis.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runEABtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${emotionalAnalysis.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runInterpretationBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${interpretation.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runSuggestionsBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${suggestions.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runThoughtsBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${thoughts.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runSummarizationBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${summarization.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runIntentDetectionBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${intentDetection.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runKeywordsExtractionBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${keywordsExtraction.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runSentimentAnalysisBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${sentimentAnalysis.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runContextAnalysisBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${contextAnalysis.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runAnomalyDetectionBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${anomalyDetection.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runPersonalizationBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${personalization.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    document.getElementById('runResponseVariationsBtn').addEventListener('click', async (event) => {
        queryHistory += `Assistant: ${responseVariations.textContent}\n`;
        resubmitQuery(queryHistory + '\nUser: ' + originalQuery);
    });

    async function generateAnalysis() {
        clearFields();
        runBtn.disabled = true;
        runBtn.innerText = 'Diving...';
        thoughtsSpinner.style.display = 'block';

        var apiKey = document.getElementById('apiKey').value;
        var query = document.getElementById('query').value;
        var model = document.getElementById('modelSelect').value;
        var useSystemMsg = document.getElementById('systemMsg').value;
        var temperature = document.getElementById('temperature').value;
        var top_p = document.getElementById('top_p').value;
        var response = await fetch('/generate-analysis', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: `query=${encodeURIComponent(query)}&api_key=${encodeURIComponent(apiKey)}&model=${encodeURIComponent(model)}&sm=${encodeURIComponent(useSystemMsg)}&temperature=${encodeURIComponent(temperature)}&top_p=${encodeURIComponent(top_p)}`
        });

        var result = await response.json();
        if (result.error) {
            if(result.error == 'BAD_PARSE') {
                document.getElementById('query').value = "!![GPT-Diver] BAD_PARSE_ERROR. Result :\n" + result.result;
            } else {
                alert('Error: ' + result.error);
            }
        } else {
            answer.textContent = result.answer;
            interpretation.textContent = result.interpretation;
            emotionalAnalysis.textContent = result.emotional_analysis;
            thoughts.textContent = result.thoughts;
            suggestions.textContent = result.suggestions;
            analysis.textContent = result.analysis;
            summarization.textContent = result.summarization;
            intentDetection.textContent = result.intent_detection;
            keywordsExtraction.textContent = result.keywords_extraction;
            sentimentAnalysis.textContent = result.sentiment_analysis;
            contextAnalysis.textContent = result.context_analysis;
            anomalyDetection.textContent = result.anomaly_detection;
            personalization.textContent = result.personalization;
            responseVariations.textContent = result.response_variations; 
        }

        thoughtsSpinner.style.display = 'none';
        runBtn.disabled = false;
        runBtn.innerText = 'Dive In';
    }

    async function generateGptPatois() {
        var apiKey = document.getElementById('apiKey').value;
        var query = document.getElementById('query').value;
        var model = document.getElementById('modelSelect').value;
        patoisBtn.disabled = true;
        runBtn.disabled = true;
        var response = await fetch('/generate-patois', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: `query=${encodeURIComponent(query)}&api_key=${encodeURIComponent(apiKey)}&model=${encodeURIComponent(model)}`
        });

        var result = await response.json();
        if (result.error) {
            document.getElementById('query').value = "!![GPT-Diver] CONVERSION_ERROR :\n" + result.error;
        } else {
            document.getElementById('query').value = result.answer;
            
        }
        patoisBtn.disabled = false;
        runBtn.disabled = false;
    }

    async function resubmitQuery(newQuery) {
        document.getElementById('query').value = newQuery;
        generateAnalysis();
    }

    function clearFields() {
        answer.textContent = '';
        analysis.textContent = '';
        interpretation.textContent = '';
        emotionalAnalysis.textContent = '';
        thoughts.textContent = '';
        suggestions.textContent = '';
        summarization.textContent = '';
        intentDetection.textContent = '';
        keywordsExtraction.textContent = '';
        sentimentAnalysis.textContent = '';
        contextAnalysis.textContent = '';
        anomalyDetection.textContent = '';
        personalization.textContent = '';
        responseVariations.textContent = '';
    }
});
