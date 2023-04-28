from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    connection_string = "mongodb+srv://user:spilock@spilock.krn09rf.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(connection_string, connect=False)

    db = client["user_security_questions"]
    return db


def insert_database():
    db = get_database()
    collection_name = db["user_1"]

    # Example of a Security Question [Question/Answer Pair]
    pair_1 = {
        "question": "What is your favourite food",
        "answer": "Fish",
    }
    collection_name.insert_one(pair_1)


def query_question():
    db = get_database()

    collection_name = db["user_1"]

    security_question = collection_name.find()
    for question in security_question:
        print(question['question'])
        question = question['question']
        return question


def query_answer(question):
    db = get_database()

    collection_name = db["user_1"]

    security_question = collection_name.find()
    for q in security_question:
        if q['question'] == question:
            print(q['answer'])
            valid_answer = q['answer']
            return valid_answer
