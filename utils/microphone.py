class microphone:
    def __init__(self, mic = ""):
        self._mic = mic

    # getter method
    def get_response(self):
        return self._mic

    # setter method
    def set_response(self, response):
        self._mic = response
