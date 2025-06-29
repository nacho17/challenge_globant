from pydantic import BaseModel
from typing import List, Optional

class DepartmentSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class JobSchema(BaseModel):
    id: int
    job: str

    class Config:
        orm_mode = True

class EmployeeSchema(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

    class Config:
        orm_mode = True
