class rfid:
    def __init__(self, id = 0):
        self._id = id

    # getter method
    def get_rfid(self):
        return self._id

    # setter method
    def set_rfid(self, tag):
        self._id = tag