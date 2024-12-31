''' Task 6: Web deployment of the application using Flask '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' emotion detection '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the score and dominant emotion from the response
    score_anger = response['anger']
    score_disgust = response['disgust']
    score_fear = response['fear']
    score_joy = response['joy']
    score_sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Handle cases where dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    # Return a formatted string with the score and dominant emotion
    return (
        f"For the given statement, the system response is:\n"
        f"'anger': {score_anger}, 'disgust': {score_disgust}, "
        f"'fear': {score_fear}, 'joy': {score_joy}, "
        f"and 'sadness': {score_sadness}.\n"
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' render index.html '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
