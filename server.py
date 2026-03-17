''' this is server py file which is main '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' method to call the emotion_detection '''
    text_to_analyze  = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    emotion = result['dominant_emotion']
    if emotion is None:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is {result}. "
        f"The dominant emotion is {result['dominant_emotion']}."
        )

@app.route("/")
def render_index_page():
    ''' this is docstring for the methdo'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
