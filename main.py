from fastapi import FastAPI
from maternal_app.db import Base, engine
from maternal_app.routers import mothers

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Maternal Health Tracker")

@app.get("/")
def root():
    return {"message": "Welcome to the Maternal Health Tracker API"}

# Register routers
app.include_router(mothers.router, prefix="/mothers", tags=["Mothers"])
