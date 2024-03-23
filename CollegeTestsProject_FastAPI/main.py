from fastapi import FastAPI, Body
from fastapi import responses
from fastapi.encoders import jsonable_encoder
import pydantic
from Models.listQuestions import ListQuestions


webApp = FastAPI()

@webApp.post("/createtest/")
def createTest(data = Body()):
    try:
        question_entity = ListQuestions(**data)
        print(question_entity)
    except pydantic.ValidationError as ex:
        print(ex.errors())