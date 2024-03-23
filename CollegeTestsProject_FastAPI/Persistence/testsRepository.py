from pymongo import MongoClient
import sys
import json

sys.path.append("../Models")

from Models.listQuestions import ListQuestions
from Models.question import Question

class TestRepository:
    def __init__(self, context : MongoClient):
        self.__context : MongoClient = context

    def create_test(self, question: Question):
        print(question)
        test_in_json = json.dumps(question, default=lambda ob: ob.__dict__)
        db = self.__context.get_database(name="tests")
        db["questions"].insert_one(vars(question))
        