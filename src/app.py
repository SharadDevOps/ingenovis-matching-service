# matching service v1 - initial deployment aaaa
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/ready')
def ready():
    return jsonify({"status": "ready"}), 200

@app.route('/match', methods=['POST'])
def match():
    return jsonify({
        "message": "matching pipeline placeholder",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "brand": os.getenv("BRAND", "unknown")
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)