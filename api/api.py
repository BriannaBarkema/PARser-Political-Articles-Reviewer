# Flask API

from flask import Flask, request, jsonify

# Flask template to render HTML
from flask import render_template

app = Flask(__name__)

# Get request with query parameters
@app.route('/analyze', methods=['GET'])
def get_api():
    # Get query parameters
    text = request.args.get('text')
    return render_template('analysis.html', text=text)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)