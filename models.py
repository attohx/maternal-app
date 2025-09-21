from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Mother(Base):
    __tablename__ = "mothers"   # table name in the database
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    due_date = Column(Date)

    checkins = relationship("CheckIn", back_populates="mother")  # link to check-ins

class CheckIn(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(Integer, ForeignKey("mothers.id"))  # connect to mother
    date = Column(Date)
    weight = Column(Integer)
    blood_pressure = Column(String)
    notes = Column(String)

    mother = relationship("Mother", back_populates="checkins")  # link back
