from backend.database import Base

# from datetime import datetime as dt, timezone as tz
from sqlalchemy import Column, Integer, String, Float


class Iris(Base):
    __tablename__ = "iris"
    id = Column(Integer, primary_key=True, index=True)
    species = Column(String(100), nullable=False)
    SepalLengthCm = Column(Float(precision=1), nullable=False)
    SepalWidthCm = Column(Float(precision=1), nullable=False)
    PetalLengthCm = Column(Float(precision=1), nullable=False)
    PetalWidthCm = Column(Float(precision=1), nullable=False)
