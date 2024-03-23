from fastapi import FastAPI, Body
from fastapi import responses
from fastapi.encoders import jsonable_encoder
import pydantic

from Models.listQuestions import ListQuestions
from Environment.environment import Environment
from Persistence.applicationContext import ApplicationContext

appEnvironmetn = Environment()


webApp = FastAPI()

@webApp.post("/createtest/")
def createTest(data = Body()):
    try:
        question_entity = ListQuestions(**data)
        print(question_entity)
    except pydantic.ValidationError as ex:
        print(ex.errors())