from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import pydantic
import os

from Models.test import Test
#from Environment.environment import Environment 
from Persistence.applicationContext import ApplicationContext
from Persistence.testsRepository import TestsRepository

app_dbcontext = ApplicationContext(os.environ["CONNECTION_TO_MONGODB"])

repository = TestsRepository(app_dbcontext.context)

web_server = FastAPI()

@web_server.post("/createtest/")
def create_test(data: Test):
    try:
        repository.create_test(data)
    except pydantic.ValidationError as ex:
        return Response(status_code=400)


@web_server.get("/gettitles/")
def get_titles():
    titles = repository.get_titles()
    json_data = jsonable_encoder(titles)
    return JSONResponse(content=json_data)


@web_server.get("/gettest/{title}")
def get_test(title: str):
    response_dict = repository.get_test(title)
    response_dict.pop("_id")
    json_data = jsonable_encoder(response_dict)
    return JSONResponse(json_data)


@web_server.put("/updatetest/{title}")
def update_test(data : Test, title : str):
    try:
        repository.update_test(title=title, _test=data)
        return Response(status_code=200)
    except pydantic.ValidationError as ex:
        return Response(status_code=400)


@web_server.delete("/deletetest/{title}")
def delete_test(title : str):
    repository.delete_test(title)
    return Response(status_code=200)