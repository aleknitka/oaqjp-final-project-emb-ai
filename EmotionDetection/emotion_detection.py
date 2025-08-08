"""main emotion detection function"""

import json
import requests
from constants import HEADER_API, EMOTION_API_URL, NULL_RESPONSE

__all__ = ["emotion_detector"]


def emotion_detector(text_to_analyze: str) -> dict:
    """
    Function to detect emotions in a given text.
    Handles blank input and API error responses.
    """
    if not text_to_analyze.strip():
        # Return dict with all keys as None for blank input
        return {k: None for k in NULL_RESPONSE}

    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(EMOTION_API_URL, json=payload, headers=HEADER_API)

    if response.status_code == 400:
        # Return dict with all keys as None for API 400 error
        return {k: None for k in NULL_RESPONSE}

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    label, __ = max(emotions.items(), key=lambda item: item[1])
    emotions["dominant_emotion"] = label

    return emotions
