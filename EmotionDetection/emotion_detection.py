import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse): 
    """Return the emotion for the supplied text."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    # parse the json response
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion'] 
    max_key = max(emotion_dict, key=emotion_dict.get)
    max_val = emotion_dict[max_key]
    emotion_dict.update({"dominant_emotion": max_key})
    return emotion_dict
    