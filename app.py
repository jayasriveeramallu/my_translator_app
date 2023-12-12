from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', translation=None, error=None)

@app.route('/translate', methods=['POST'])
def translate():
    api_key = '2dea3cfc68msh12a996e57067712p1abb53jsnb3b1e6331fe9'  # Replace with your RapidAPI key
    text_to_translate = request.form['text']
    target_language = request.form['language']

    # Make API request to Google Translator
    url = "https://google-translator9.p.rapidapi.com/v2"
    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'google-translator9.p.rapidapi.com'
    }
    payload = {
        'q': text_to_translate,
        'source': 'en',
        'target': target_language,
        'format': 'text'
    }
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the response
            translated_text = response.json()['data']['translations'][0]['translatedText']
            return render_template('index.html', translation=translated_text, error=None)
        except KeyError as e:
            return render_template('index.html', error=f'Error parsing response: {str(e)}')
    else:
        return render_template('index.html', error=f'Error in API request: {response.status_code}')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
