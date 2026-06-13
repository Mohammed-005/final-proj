import os
import sys
from flask import Flask, jsonify

PORT = 7000

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "v1")
FAIL_TRIGGER = os.environ.get("FALSE_TRIGGER", "false")

@app.route('/')
def home():
    if FAIL_TRIGGER.lower() == 'true':
        return jsonify ({
            "status":"error",
            "message": f"Critical: Application crash simulated on version {APP_VERSION}"
            }), 500

    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "message": "Secure payment gateway processing traffic normally."
        }), 200

@app.route('/health')
def health():
    if FAIL_TRIGGER.lower() == 'true':
        sys.exit(1)
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
