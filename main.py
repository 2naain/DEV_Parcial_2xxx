from typing import List
from db import SessionDep, create_all_tables
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from db import  SessionDep, create_all_tables
from sqlmodel import select
from model import DogBase,DogId, DogUpdate
from operations.operations_dog import DogUpdate
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
