from sqlmodel import Field, SQLModel

from datetime import datetime


class Dog(SQLModel, table = True):
    __tablename__ = "Dogs"
id = int= Field(primary_key=True)

name: str= Field()
size: str= Field()
dangerous: bool = Field()
sterilized: bool = Field()
breed: str = Field()


    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )
