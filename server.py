from flask import Flask, render_template, jsonify
import requests
from EmotionDetection import emotion_detector

app = Flask('__name__')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400
    result = emotion_detector(text)
    return jsonify({"result": result})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
