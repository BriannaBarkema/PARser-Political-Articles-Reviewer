from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from gpt import analyze_misinformation_and_bias

app = Flask(__name__)
CORS(app, support_credentials=True) # Enable CORS for the API, allowing requests from any origin


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        # they should have sent a json with one key, 'article', which is the article to be analyzed
        data = request.get_json()
        article = data['article']
        result = analyze_misinformation_and_bias(article) # this returns a dictionary
        return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True)