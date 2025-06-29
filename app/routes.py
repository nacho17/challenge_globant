from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/{table_name}")
def upload_csv(table_name: str, db: Session = Depends(get_db)):
    filepath = f"data/{table_name}.csv"
    model_map = {
        "departments": models.Department,
        "jobs": models.Job,
        "hired_employees": models.Employee
    }
    model = model_map.get(table_name)
    if not model:
        return {"error": "Invalid table"}
    crud.load_csv_to_db(filepath, model, db)
    return {"status": f"{table_name} loaded successfully"}

@router.post("/batch/{table_name}")
def insert_batch(table_name: str, data: list[dict], db: Session = Depends(get_db)):
    model_map = {
        "departments": models.Department,
        "jobs": models.Job,
        "hired_employees": models.Employee
    }
    model = model_map.get(table_name)
    if not model:
        return {"error": "Invalid table"}
    crud.insert_batch(db, model, data)
    return {"status": f"{len(data)} records inserted into {table_name}"}
