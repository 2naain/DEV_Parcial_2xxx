from typing import List
from db import SessionDep, create_all_tables
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from db import  SessionDep, create_all_tables
from sqlmodel import select
from model import DogBase,DogId, DogUpdate
from operations.operations_dog import(
    create_dog_db, update_dog_db,
    delete_dog_db, get_one_dog_db,
)
app = FastAPI()


app = FastAPI(lifespan=create_all_tables)

@app.post("/dog",response_model=DogId)
async def create_dog(dog: DogBase,session: SessionDep):
    return create_dog_db(dog,session)



@app.get("/dog/{id}",response_model=DogId)
async def get_one_dog(id: int,session: Session = Depends(SessionDep)):
    dog= get_one_dog_db(id,session)
    if not dog:
        raise HTTPException(status_code=404, detail="Dog with id {id} not found")
    return dog


@app.patch("/dog/{id}", response_model=DogId)
async def update_dog(id: int,dog: DogUpdate,session: Session):
    updated = get_one_dog_db(id,session)
    if not updated:
        raise HTTPException(status_code=404, detail="Dog with id {id} not found")
    return updated



endpoint showalldogs
