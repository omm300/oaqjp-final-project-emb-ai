
"""Flask web application for Watson NLP emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the emotion detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Process text and return its emotion analysis."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if not result or result["dominant_emotion"] is None:
        return "Emotion service unavailable. Please try again later.", 503

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
