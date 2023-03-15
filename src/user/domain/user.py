from datetime import date

# pylint: disable=no-name-in-module
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    birth_date: date
    gender: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
