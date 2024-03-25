from pydantic import BaseModel
from Models.question import Question

class Test(BaseModel):
    title: str
    questions: list[Question]
    
