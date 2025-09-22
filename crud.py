from sqlalchemy.orm import Session
from maternal_app import models, schemas

def create_mother(db: Session, mother: schemas.MotherCreate):
    new_mother = models.Mother(**mother.dict())
    db.add(new_mother)
    db.commit()
    db.refresh(new_mother)
    return new_mother

def get_mothers(db: Session):
    return db.query(models.Mother).all()

def get_mother(db: Session, mother_id: int):
    return db.query(models.Mother).filter(models.Mother.id == mother_id).first()

def update_mother(db: Session, mother_id: int, update: schemas.MotherUpdate):
    mother = get_mother(db, mother_id)
    if not mother:
        return None
    for field, value in update.dict(exclude_unset=True).items():
        setattr(mother, field, value)
    db.commit()
    db.refresh(mother)
    return mother

def delete_mother(db: Session, mother_id: int):
    mother = get_mother(db, mother_id)
    if not mother:
        return None
    db.delete(mother)
    db.commit()
    return mother
