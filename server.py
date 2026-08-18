''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the emotionscores
        and the dominant emotion for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is ",
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']},"
        f" 'joy': {result['joy']} and 'sadness': {result['sadness']}. ",
        f"The dominant emotion is {result['dominant_empotion']}."
        )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
