from flask import Flask, render_template, jsonify, request
import requests
from EmotionDetection import emotion_detector

app = Flask('__name__')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def analyse():
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400
    try:
        result = emotion_detector(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Upstream error: {e}"}), 502

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
