from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from maternal_app import schemas, crud
from maternal_app.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.MotherResponse)
def create_mother(mother: schemas.MotherCreate, db: Session = Depends(get_db)):
    return crud.create_mother(db, mother)

@router.get("/", response_model=List[schemas.MotherResponse])
def get_mothers(db: Session = Depends(get_db)):
    return crud.get_mothers(db)

@router.get("/{mother_id}", response_model=schemas.MotherResponse)
def get_mother(mother_id: int, db: Session = Depends(get_db)):
    mother = crud.get_mother(db, mother_id)
    if not mother:
        raise HTTPException(status_code=404, detail="Mother Not in Records")
    return mother

@router.put("/{mother_id}", response_model=schemas.MotherResponse)
def update_mother(mother_id: int, update: schemas.MotherUpdate, db: Session = Depends(get_db)):
    updated = crud.update_mother(db, mother_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Mother not in Records")
    return updated

@router.delete("/{mother_id}")
def delete_mother(mother_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_mother(db, mother_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mother not in Records")
    return {"message": "Mother deleted successfully"}
