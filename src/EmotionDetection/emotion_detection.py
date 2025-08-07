import requests
import json

def emotion_detector(text_to_analyze:str) -> dict:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    payload = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=payload, headers=header)

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]['emotion']

    label, __ = max(emotions.items(), key=lambda item: item[1])
    
    emotions['dominant_emotion'] = label
    # Returning a dictionary containing sentiment analysis results
    return emotions