from pymongo import MongoClient

mongoClient = MongoClient("mongodb://student:1234@localhost:27010/tests")

mongoDb = mongoClient["test1_db"]

collection = mongoDb["users"]