from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from frontend.app.library.helpers import openfile
from frontend.app.viz.iris_plot import *

app = FastAPI()

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


##Test Iris Viz
@app.route("/")
def root():
    return page.render(resources=CDN.render())


@app.route("/plot")
def plot():
    p = make_plot("petal_width", "petal_length")
    return json.dumps(json_item(p, "myplot"))  # default theme applied


@app.route("/plot2")
def plot2():
    p = make_plot("sepal_width", "sepal_length")
    return json.dumps(json_item(p, theme=gray_theme))  # specific theme (gray) applied
