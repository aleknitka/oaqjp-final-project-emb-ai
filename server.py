from flask import Flask, render_template
from EmotionDetection import emotion_detector

app = Flask('__name__')

@app.route("/")
def index():
    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)