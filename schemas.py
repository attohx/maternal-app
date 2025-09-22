from pydantic import BaseModel,  Field, constr, field_validator
from datetime import date
from typing import Optional

class MotherBase(BaseModel):
    name :  constr(strip_whitespace=True, min_length=2, max_length=100)
    age : int = Field(..., ge=12,le=60, description= "Age mst be between 12 and 60")
    due_date: Optional[date] = None
    medical_notes: str | None = None

    @field_validator("due_date")
    def validate_due_date(cls, v):
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class MotherCreate(MotherBase):
    pass


class MotherUpdate(BaseModel):
    name: Optional[constr(strip_whitespace=True, min_length=2, max_length=100)]
    age: Optional[int] = Field(None, ge=12, le=60)
    due_date: Optional[date] = None
    medical_notes: Optional[str] = Field(None, max_length=500)

    @field_validator("due_date")
    def validate_due_date(cls, v):
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v


class MotherResponse(MotherBase):
    id: int

    class Config:
        orm_mode = True