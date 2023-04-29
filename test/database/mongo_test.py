import unittest
from pymongo import MongoClient

from src.database.mongo import query_question, query_answer


class TestDatabase(unittest.TestCase):

    def set_up(self):
        # setup a test database
        self.connection_string = "mongodb+srv://user:spilock@spilock.krn09rf.mongodb.net/?retryWrites=true&w=majority"
        self.test_client = MongoClient(self.connection_string, connect=False)
        self.test_db = self.test_client["user_security_questions"]
        self.test_collection = self.test_db["user_1"]
        self.test_question = "What is your favourite food"
        self.test_answer = "Fish"
        self.test_collection.insert_one({"question": self.test_question, "answer": self.test_answer})

    def test_query_question(self):
        self.set_up()
        # test if the correct question is returned
        question = query_question()
        self.assertEqual(question, self.test_question)

    def test_query_answer(self):
        self.set_up()
        # test if the correct answer is returned
        answer = query_answer(self.test_question)
        self.assertEqual(answer, self.test_answer)

    def tear_down(self):
        # remove the test database after each test
        self.test_client.drop_database("user_1")
