from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze  = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze )
    emotion = result['dominant_emotion']
    return "For the given statement, the system response is {}. The dominant emotion is {}.".format(result,result['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)