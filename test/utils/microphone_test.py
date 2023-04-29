import unittest

from utils.microphone import microphone


class TestMicrophone(unittest.TestCase):
    def test_set_response(self):
        mic = microphone()
        mic.set_response("Hello")
        self.assertEqual(mic.get_response(), "Hello")

    def test_get_response(self):
        mic = microphone("Hi")
        self.assertEqual(mic.get_response(), "Hi")


if __name__ == '__main__':
    unittest.main()
