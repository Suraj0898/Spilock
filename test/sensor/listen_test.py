import unittest
from unittest.mock import Mock

from src.sensor.listen import listen


class ListenTestCase(unittest.TestCase):
    def test_listen(self):
        # Create a mock microphone object
        mock_microphone = Mock()
        expected_response = "hello world"
        mock_microphone.get_response.return_value = expected_response

        # Replace the actual Microphone class with the mock object
        import speech_recognition as sr
        sr.Microphone = Mock(return_value=mock_microphone)

        # Call the listen() function and check the result
        result = listen()
        self.assertEqual(result, mock_microphone)

        # Check that the microphone's get_response() method was called
        mock_microphone.get_response.assert_called_once()
        # Check that the response returned by the microphone is correct
        self.assertEqual(mock_microphone.get_response(), expected_response)
