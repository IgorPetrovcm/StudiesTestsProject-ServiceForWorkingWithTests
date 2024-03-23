from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import json
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
def create_test(data: ListQuestions):
    try:
        repository.create_test(data)
    except pydantic.ValidationError as ex:
        print(ex.errors())

@webApp.get("/gettitles/")
def get_titles():
    titles = repository.get_titles()
    response_json = json.dumps(titles, default=lambda o: o.__dict__)
    return JSONResponse(response_json)