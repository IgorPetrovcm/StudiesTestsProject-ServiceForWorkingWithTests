from pymongo import MongoClient
import sys
from bson import json_util
import json
sys.path.append("../Models")

from Models.test import Test
from Models.question import Question

class TestRepository:
    def __init__(self, context : MongoClient):
        self.__context : MongoClient = context

    def __test_to_json_parse(test : Test) -> str:
        questions_json = ""
        i = 1
        for question in test.questions:
            if i == len(test.questions):
                questions_json += json.dumps(question, default=lambda o: o.__dict__)
                break
            questions_json += json.dumps(question, default=lambda o: o.__dict__) + ","
            i += 1

        title_json = "\"title\": \"" + test.title + "\"" 

        return "{" + title_json + "," + "\"questions\":" + "[" + questions_json + "]" + "}"

    def create_test(self, test: Test):
        db = self.__context["tests"]

        db["tests"].insert_one(json.loads(self.__test_to_json_parse(test)))

    def get_titles(self):
        db = self.__context["tests"]
        cursor = db["tests"].find()

        titles = []
        for test in cursor:
            titles.append(test["title"])

        return titles
    
    def get_test(self, title : str):
        db = self.__context["tests"]
        cursor = db["tests"].find({"title": title})

        for key in cursor:
            return key
        