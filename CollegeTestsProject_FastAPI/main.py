from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import json
import pydantic
from pymongo import MongoClient

from Models.question import Question
from Models.test import Test
from Environment.environment import Environment
from Persistence.applicationContext import ApplicationContext
from Persistence.testsRepository import TestRepository

appEnvironmetn = Environment()
repository = TestRepository(MongoClient(appEnvironmetn.get_appsetting_value("ConnectionToMongoDefault")))

webApp = FastAPI()

@webApp.post("/createtest/")
def create_test(data: Test):
    try:
        repository.create_test(data)
    except pydantic.ValidationError as ex:
        print(ex.errors())

@webApp.get("/gettitles/")
def get_titles():
    titles = repository.get_titles()
    response_json = json.dumps(titles, default=lambda o: o.__dict__)
    return JSONResponse(response_json)

@webApp.get("/gettest/{title}")
def get_test(title: str):
    response_dict = repository.get_test(title)
    print (response_dict)
    response_dict.pop("_id")
    json_response = json.dumps(response_dict)

    return JSONResponse(json_response )

@webApp.put("/updatetest/{title}")
def update_test(title : str):
    