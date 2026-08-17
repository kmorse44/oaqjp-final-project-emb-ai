"""Flask web application for sentiment analysis."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the HTML index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """Analyze text submitted through the web page."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    response_str = ""
    for item in response:
        response_str += "'" + item + "'" + ': ' + str(response[item]) + ', '
    dominant = response["dominant_emotion"]
    
    return (
        f"For the given statement, the system response is "
        f"{response_str}."
        f"The dominant emotion is {dominant}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)