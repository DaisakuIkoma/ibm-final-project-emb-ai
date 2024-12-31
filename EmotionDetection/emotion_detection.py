''' the Emotion Predict function of the Watson NLP Library '''
import json
import requests

def emotion_detector(text_to_analyse):
    '''Emotion Detection function.'''
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=input_json, headers=header, timeout=10)
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotion = formatted_response['emotionPredictions'][0]['emotion']
            emotion['dominant_emotion'] = max(emotion, key=emotion.get)
        else:
            # error handling including status_code = 400
            emotion = None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        emotion = None

    return emotion
