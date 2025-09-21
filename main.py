import maternal_app.db
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Maternal Health Tracker")

# In-memory "database"
mothers_data = []

# Define input model
class MotherData(BaseModel):
    name: str
    age: int
    systolic_bp: int
    diastolic_bp: int
    blood_sugar: float

@app.get("/")
def root():
    return {"message": "Welcome to the Maternal Health Tracker API"}

@app.post("/add_mother")
def add_mother(data: MotherData):
    mothers_data.append(data.dict())
    return {"message": "Mother's data added successfully", "data": data}

@app.get("/all_mothers")
def get_all_mothers():
    return {"mothers": mothers_data}

@app.get("/mother/{name}")
def get_mother(name: str):
    for mother in mothers_data:
        if mother["name"].lower() == name.lower():
            return mother
    return {"error": "Mother not found"}
