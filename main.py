from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from maternal_app.db import get_db, Base, engine
from maternal_app.models import Mother
from maternal_app import schemas

# Make sure tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Maternal Health Tracker")

@app.get("/")
def root():
    return {"message": "Welcome to the Maternal Health Tracker API"}

@app.post("/mothers/", response_model=schemas.MotherResponse)
def create_mother(mother: schemas.MotherCreate, db: Session = Depends(get_db)):
    new_mother = Mother(**mother.dict())
    db.add(new_mother)
    db.commit()
    db.refresh(new_mother)
    return new_mother

@app.get("/mothers/", response_model=list[schemas.MotherResponse])
def get_mothers(db: Session = Depends(get_db)):
    return db.query(Mother).all()

@app.get("/mothers/{mother_id}", response_model=schemas.MotherResponse)
def get_mother(mother_id: int, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother:
        raise HTTPException(status_code=404, detail="Mother Not in Records")
    return mother

@app.put("/mothers/{mother_id}", response_model=schemas.MotherResponse)
def update_mother(mother_id: int, update: schemas.MotherUpdate, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother:
        raise HTTPException(status_code=404, detail="Mother not in records")

    for field, value in update.dict(exclude_unset=True).items():
        setattr(mother, field, value)

    db.commit()
    db.refresh(mother)
    return mother

@app.delete("/mothers/{mother_id}")
def delete_mother(mother_id: int, db: Session = Depends(get_db)):
    mother = db.query(Mother).filter(Mother.id == mother_id).first()
    if not mother: 
        raise HTTPException(status_code=404, detail="Mother not in Records")
    
    db.delete(mother)
    db.commit()
    return {"message": "Mother deleted successfully"}
