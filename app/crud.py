import pandas as pd
from sqlalchemy.orm import Session
from . import models

def load_csv_to_db(filepath: str, model, db: Session):
    df = pd.read_csv(filepath)
    records = [model(**row) for row in df.to_dict(orient="records")]
    db.add_all(records)
    db.commit()

def insert_batch(db: Session, model, data: list[dict]):
    records = [model(**item) for item in data]
    db.add_all(records)
    db.commit()
