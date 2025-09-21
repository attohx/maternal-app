from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date

from maternal_app.db import get_db, Base, engine
from maternal_app.models import Mother

# Make sure tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Maternal Health Tracker")

# -------------------------------
# Pydantic Schemas
# -------------------------------
class MotherCreate(BaseModel):
    name: str
    age: int
    due_date: date | None = None
    medical_notes: str | None = None

class MotherUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    due_date: date | None = None
    medical_notes: str | None = None


# -------------------------------
# Database CRUD endpoints
# -------------------------------

@app.get("/")
def root():
    return {"message": "Welcome to the Maternal Health Tracker API"}


# Create (POST)
@app.post("/mothers/")
def create_mother(mother: MotherCreate, db: Session = Depends(get_db)):
    new_mother = Mother(
        name=mother.name,
        age=mother.age,
        medical_notes=mother.medical_notes
    )
    db.add(new_mother)
    db.commit()
    db.refresh(new_mother)
    return new_mother


# Read all
@app.get("/mothers/")
def get_mothers(db: Session = Depends(get_db)):
    return db.query(Mother).all()


# Read one
@app.get("/mothers/{mother_id}")
def get_mother(mother_id: int, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother:
        raise HTTPException(status_code=404, detail="Mother Not in Records")
    return mother


# Update
@app.put("/mothers/{mother_id}")
def update_mother(mother_id: int, update: MotherUpdate, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother:
        raise HTTPException(status_code=404, detail="Mother not in records")

    if update.name is not None:
        mother.name = update.name
    if update.age is not None:
        mother.age = update.age
    if update.medical_notes is not None:
        mother.medical_notes = update.medical_notes

    db.commit()
    db.refresh(mother)
    return mother


# Delete
@app.delete("/mothers/{mother_id}")
def delete_mother(mother_id: int, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother: 
        raise HTTPException(status_code=404, detail="Mother not in Records")
    
    db.delete(mother)
    db.commit()
    return {"message": "Mother deleted successfully"}
