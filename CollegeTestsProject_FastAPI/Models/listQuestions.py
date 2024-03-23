from pydantic import BaseModel
from Models.question import Question

class ListQuestions(BaseModel):
    questions: list[Question]