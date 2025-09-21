from sqlalchemy import Column, Integer, String, Date
from maternal_app.db import Base

class Mother(Base):
    __tablename__ = "mothers"   # table name in the database
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    due_date = Column(Date, nullable=True)
    medical_notes = Column(String, nullable=True)
