import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    print(response.status_code)
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response.get(
            "emotionPredictions", [{}]
        )[0].get("emotion", {})

    dominant_emotion = max(emotions, key=emotions.get) if emotions else None

    if response.status_code == 400:

        return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
    
    else:

        return {
                "anger": emotions.get("anger"),
                "disgust": emotions.get("disgust"),
                "fear": emotions.get("fear"),
                "joy": emotions.get("joy"),
                "sadness": emotions.get("sadness"),
                "dominant_emotion": dominant_emotion
            }