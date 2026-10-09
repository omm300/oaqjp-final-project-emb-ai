
import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detection


class TestEmotionDetection(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.01,
                    "fear": 0.02,
                    "joy": 0.94,
                    "sadness": 0.02,
                }
            }]
        }

        result = emotion_detection.emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.90,
                    "disgust": 0.02,
                    "fear": 0.02,
                    "joy": 0.02,
                    "sadness": 0.04,
                }
            }]
        }

        result = emotion_detection.emotion_detector("I am angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.02,
                    "fear": 0.02,
                    "joy": 0.04,
                    "sadness": 0.90,
                }
            }]
        }

        result = emotion_detection.emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_blank_input(self):
        result = emotion_detection.emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
