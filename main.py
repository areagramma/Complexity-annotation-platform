import csv
import uvicorn
from fastapi import FastAPI, Request, Path
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas
from starlette.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from tokenizare import tokenize

app = FastAPI()
templates = Jinja2Templates(directory = "templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

df = pandas.read_csv('propozitii.csv')
corpus = df['text_propozitie']

# Hello World route
@app.get("/")
def index():

    file = open('propozitii.csv')
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

    return {'data': {'count': row_count - 1}}

# TESTE:

# de facut get cu query parameters pt fiecare propozitie deja tokenizata
# folosim spicy, script separat
'''
@app.get('/propozitii', response_class = HTMLResponse)
async def list(request: Request):
    my_corpus = corpus
    tokenizate = []
    for prop in my_corpus:
        tokenizate.append(tokenize(prop))
    #print(len(tokenizate))
    return templates.TemplateResponse("annotation.html", {"request": request, "corpus": tokenizate})
'''

@app.get("/param")
def param(id):
    return {'data': id}

@app.get('/propozitii', response_class = HTMLResponse)
async def list(id_prop: int, request: Request):
    my_corpus = corpus
    tokenizate = []
    for prop in my_corpus:
        tokenizate.append(tokenize(prop))
    return templates.TemplateResponse("annotation.html", {"id_prop": id_prop, "request": request, "corpus": tokenizate})


@app.get('/index', response_class = HTMLResponse)
async def index2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/basic_identity', response_class = HTMLResponse)
async def index2(request: Request):
    return templates.TemplateResponse("basic_identity.html", {"request": request})
