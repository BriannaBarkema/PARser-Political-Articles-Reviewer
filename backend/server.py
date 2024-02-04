# server.py

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from gpt import analyze_misinformation_and_bias
import os

app = Flask(__name__)
CORS(app, support_credentials=True) # Enable CORS for the API, allowing requests from any origin

# Get request with query parameters
@app.route('/analyze', methods=['GET'])
def analyze():
    text = request.args.get('text')
    return render_template('app.html', text=text)

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        # they should have sent a json with one key, 'article', which is the article to be analyzed
        data = request.get_json()
        article = data['article']
        result = analyze_misinformation_and_bias(article) # this returns a dictionary
        return jsonify(result)

@app.route('/static/<path:path>', methods=['GET'])
def static_files(path):
    print("Received request for static file: ", path)
    return send_from_directory('static', path)

@app.route('/favicon.ico', methods=['GET'])
def fav():
    print("Received request for favicon.ico")
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')
    
# catch all other routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Received request for path: ", path)
    return 'You want path: %s' % path

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)