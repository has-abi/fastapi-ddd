from datetime import date

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
