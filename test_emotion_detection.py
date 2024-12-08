from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')

        result_2 = emotion_detector('I am really angry about this')
        self.assertEqual(result_1['label'], 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['label'], 'disgust')

        result_2 = emotion_detector('I am so sad about this sadness')
        self.assertEqual(result_1['label'], 'sadness')

        result_2 = emotion_detector('I am very afraid of this happening')
        self.assertEqual(result_1['label'], 'fear')

        
    unittest.main()