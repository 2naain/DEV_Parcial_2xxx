from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from model import DogBase,DogId,DogUpdate



def create_dog_db(dog: DogBase, session: Session):
    new_dog= DogId.model_validate(dog)
    session.add(new_dog)
    session.commit()
    session.refresh(new_dog)
    return new_dog


def get_one_dog_db(id: int, session: Session):
    try:
        return session.get_one(DogId, id)
    except NoResultFound:
        return None


def update_dog_db(id: int, dog_update: DogUpdate, session: Session):
    dog= get_one_dog_db(id, session)
    if dog is None:
        return None
    update_data = dog_update.model_dump(exclude_unset=True)
    dog.sqlmodel_update(update_data)
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog




def delete_dog_db(id: int, session: Session):
    try:
        dog = session.get_one(DogId, id)
        session.delete(dog)
        session.commit()
        return dog
    except NoResultFound:
        return None