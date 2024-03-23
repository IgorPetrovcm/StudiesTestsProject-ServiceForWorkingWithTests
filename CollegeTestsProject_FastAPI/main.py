from fastapi import FastAPI, Body
from fastapi import responses
from fastapi.encoders import jsonable_encoder
import pydantic
from pymongo import MongoClient

from Models.listQuestions import ListQuestions, Question
from Environment.environment import Environment
from Persistence.applicationContext import ApplicationContext
from Persistence.testsRepository import TestRepository

appEnvironmetn = Environment()
repository = TestRepository(MongoClient(appEnvironmetn.get_appsetting_value("ConnectionToMongoDefault")))

webApp = FastAPI()

@webApp.post("/createtest/")
def createTest(data: Question):
    try:
        repository.create_test(data)
    except pydantic.ValidationError as ex:
        print(ex.errors())