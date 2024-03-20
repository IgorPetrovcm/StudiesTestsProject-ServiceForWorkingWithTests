from fastapi import FastAPI, Body
from fastapi import responses
from fastapi.encoders import jsonable_encoder

webApp = FastAPI()

@webApp.post("/createtest/")
def createTest(data = Body()):
    print(data)