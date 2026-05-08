from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/personas", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="personas.html"
    )

@app.get("/Tartaro", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="Tartaro.html"
    )


