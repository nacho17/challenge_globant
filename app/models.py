from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String)

class Employee(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
