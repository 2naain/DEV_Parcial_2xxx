from typing import List

from fastapi import FastAPI

from db import  SessionDep, create_all_tables
from sqlmodel import select

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


3endpoint añadir registro a ala tabla
endpoint modificar
endpoint recuerar por #id
endpoint showalldogs
