import unittest

from utils.rfid import rfid


class TestRfid(unittest.TestCase):
    def test_get_rfid(self):
        tag_id = "12345"
        my_rfid = rfid(tag_id)
        self.assertEqual(my_rfid.get_rfid(), tag_id)

    def test_set_rfid(self):
        tag_id = "12345"
        new_tag_id = "67890"
        my_rfid = rfid(tag_id)
        my_rfid.set_rfid(new_tag_id)
        self.assertEqual(my_rfid.get_rfid(), new_tag_id)


if __name__ == '__main__':
    unittest.main()
