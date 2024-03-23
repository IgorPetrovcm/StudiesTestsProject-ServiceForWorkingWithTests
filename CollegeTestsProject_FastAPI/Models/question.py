from pydantic import BaseModel 

class Question(BaseModel):
    name: str
    answerOptions: list[str]
    answers: list[int]