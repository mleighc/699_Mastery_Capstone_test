from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from frontend.app.library.helpers import openfile
from sqlalchemy.orm import Session

import backend.crud as iris_crud
import backend.schemas as iris_schemas
import backend.models as iris_models

from backend.database import SessionLocal, engine

from bokeh.plotting import figure
from bokeh.embed import components


app = FastAPI(
    title="Dashboard Application",
    description="SI 699 Capstone Dashboard Application",
    version="1.0.0",
)

############################################
############TEST SQLite DB##################
# Initialize
iris_models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@app.post(
    "/api/v1/iris/",
    response_model=iris_schemas.Iris,
    status_code=status.HTTP_201_CREATED,
)
async def create_iris(data: iris_schemas.Iris):
    """TODO"""

    return await iris_crud.create_iris(data)


@app.delete("/api/v1/iris/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_iris(id: int):
    """Delete resource. No response is provided."""

    await iris_crud.delete_iris(id)


@app.get("/")
async def read_root() -> str:
    """TODO"""

    return "This is the iris home page."


@app.get("/api/v1/iris/{id}", response_model=iris_schemas.Iris)
async def read_iris(id: int):
    """TODO"""

    # TODO Handle query strings
    return await iris_crud.read_iris(id)


#############TEST SQLite END################
############################################


##############################################
#########FRONTEND PAGES START#################
templates = Jinja2Templates(directory="./frontend/templates")
app.mount("/static", StaticFiles(directory="./frontend/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openfile(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


#########FRONTEND PAGES END#################
############################################


############################################
############TEST BOKEH VIZ##################


#############TEST BOKEH VIZ END#############
############################################
