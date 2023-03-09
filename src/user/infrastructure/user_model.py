import enum

from sqlalchemy import Column, Date, Enum, Integer, String

from src.database import Base


class GenderEnum(str, enum.Enum):
    FEMALE = "female"
    MALE = "male"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    birth_date = Column(Date)
    gender = Column(Enum(GenderEnum), nullable=False)
