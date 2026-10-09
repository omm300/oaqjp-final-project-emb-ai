
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions in text using the Watson NLP service."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url, headers=headers, json=payload, timeout=30
    )

    if response.status_code == 400:
        return None

    response.raise_for_status()
    return response.json()
