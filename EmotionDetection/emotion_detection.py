import requests
import json


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    # Return the required dictionary with None values for invalid input
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]
 
        dominant_emotion = max(
            emotion_dict,
            key=emotion_dict.get
        )

        return {
            "anger": emotion_dict["anger"],
            "disgust": emotion_dict["disgust"],
            "fear": emotion_dict["fear"],
            "joy": emotion_dict["joy"],
            "sadness": emotion_dict["sadness"],
            "dominant_emotion": dominant_emotion
        }

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }