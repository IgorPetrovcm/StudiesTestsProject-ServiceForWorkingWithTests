from pymongo import MongoClient
import sys
from bson import json_util
import json
sys.path.append("../Models")

from Models.listQuestions import ListQuestions
from Models.question import Question

class TestRepository:
    def __init__(self, context : MongoClient):
        self.__context : MongoClient = context

    def create_test(self, test: ListQuestions):
        db = self.__context["tests"]

        questions_json = ""
        i = 1
        for question in test.questions:
            if i == len(test.questions):
                questions_json += json.dumps(question, default=lambda o: o.__dict__)
                break
            questions_json += json.dumps(question, default=lambda o: o.__dict__) + ","
            i += 1

        title_json = "\"title\": \"" + test.title + "\"" 

        json_data = "{" + title_json + "," + "\"questions\":" + "[" + questions_json + "]" + "}"

        db["tests"].insert_one(json.loads(json_data))

    def get_titles(self):
        db = self.__context["tests"]
        cursor = db["tests"].find()

        titles = []
        for test in cursor:
            titles.append(test["title"])

        return titles
        