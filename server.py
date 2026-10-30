from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionAnalyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if not isinstance(response, dict):
        return str(response)

    dominant_emotion = response.get("dominant_emotion", "unknown")
    emotion_scores = {
        key: value
        for key, value in response.items()
        if key != "dominant_emotion"
    }

Code=response.status_mode

    return (
        f"For the given statement, the system response is "
        f"{emotion_scores}. The dominant emotion is "
        f"{dominant_emotion}. Code is {Code}"
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
