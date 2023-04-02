# from datetime import datetime as datetime
from pydantic import BaseModel


class IrisBase(BaseModel):
    """TODO"""

    id: int
    species: str
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    class Config:
        orm_mode = True


class IrisCreate(IrisBase):
    pass


class Iris(IrisBase):
    id: int
    species: str

    class Config:
        orm_mode = True
