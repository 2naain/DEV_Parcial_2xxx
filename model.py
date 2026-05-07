from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class DogBase(SQLModel):
    name: str = Field(min_length=2, max_length=20)
    size: str = Field(min_length=2, max_length=20)
    dangerous: bool = Field(default=False)
    sterilized: bool = Field(default=False)
    breed: str = Field(min_length=2, max_length=20)
    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )


class DogId(DogBase, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)



class DogUpdate(SQLModel):
    name: str = Field(min_length=2, max_length=20)
    size: str = Field(min_length=2, max_length=20)
    dangerous: bool = Field(default=False)
    sterilized: bool = Field(default=False)
    breed: str = Field(min_length=2, max_length=20)
    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )



