"""Main app module"""

from flask import Flask, render_template, jsonify, request
from EmotionDetection import emotion_detector

app = Flask("__name__")


@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def analyse():
    """
    Endpoint to analyze emotions in a given text.
    """
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400
    try:
        result = emotion_detector(text)
        dominant = result.get("dominant_emotion", "unknown")
        response_str = f"For the given statement, the dominant emotion is {dominant}. All values: {result}"
        return response_str
    except Exception as e:
        return jsonify({"error": f"Upstream error: {e}"}), 502


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
