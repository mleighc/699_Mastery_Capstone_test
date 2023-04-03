import backend.models as models
import backend.schemas as schemas
from backend.database import engine
from fastapi import HTTPException
from sqlalchemy.orm import Session


async def create_iris(data: schemas.Iris):
    """TODO"""

    with Session(bind=engine, expire_on_commit=False) as session:
        iris = models.Iris(
            species=data.species,
            SepalLengthCm=data.SepalLengthCm,
            SepalWidthCm=data.SepalWidthCm,
            PetalLengthCm=data.PetalLengthCm,
            PetalWidthCm=data.PetalWidthCm,
        )
        session.add(iris)
        session.commit()
        session.refresh(iris)  # adds pk, etc.
        session.close()  # TODO redundant given context manager

        # WARN list cannot be used in an await expression
        # return schemas.RailroadRequest(**railroad.dict()) #
        return iris


async def delete_iris(id: int):
    """Delete resource."""

    with Session(bind=engine, expire_on_commit=False) as session:
        iris = session.query(models.Iris).get(id)
        if iris:
            session.delete(iris)
            session.commit()
            session.close()  # TODO redundant given context manager
        else:
            raise HTTPException(status_code=404, detail=f"id {id} not found.")


async def read_iris(id: int):
    """TODO"""

    with Session(bind=engine, expire_on_commit=False) as session:
        # WARN Iris object cannot be used in an await expression
        return session.query(models.Iris).get(id)
