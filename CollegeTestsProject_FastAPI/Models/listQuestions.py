from pydantic import BaseModel
from Models.question import Question

class ListQuestions(BaseModel):
    title: str
    questions: list[Question]
    
