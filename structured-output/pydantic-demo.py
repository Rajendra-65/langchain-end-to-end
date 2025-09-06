from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str  = 'Rajendra'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0 , lt = 10,description = 'A decimal value representing the cgpa of the student ')

new_student = {
    'age' : 22,
    'email' : 'abc@gmail.com',
    'cgpa' : 12
}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()