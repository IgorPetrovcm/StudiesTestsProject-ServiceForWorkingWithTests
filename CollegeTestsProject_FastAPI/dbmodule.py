from pymongo import MongoClient

mongoClient = MongoClient("mongodb://student:1234@localhost:27010/")

mongoDb = mongoClient["tests"]

collection = mongoDb["questions"]

'''question = {
    "name": "test1",
    "answerOptions": ["1","2"],
    "answers": [2]
}'''

questions = collection.find({})

for question in questions:
    print(question)