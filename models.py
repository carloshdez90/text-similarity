from pydantic import BaseModel


class Item(BaseModel):
    expected_response: str
    student_response: str
