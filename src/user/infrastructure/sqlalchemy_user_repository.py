from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from src.user.domain.user import User, UserCreate
from src.user.domain.user_repository import UserRepository
from src.user.infrastructure.user_data_mapper import (
    user_entity_to_model,
    user_model_to_entity,
)
from src.user.infrastructure.user_model import UserModel


class SQLAlchemyUserRepository(UserRepository):
    def __init__(
        self, session_manager: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_manager = session_manager

    def find_all(self, limit: int, skip: int) -> list[User]:
        with self._session_manager() as session:
            instances = session.query(UserModel).offset(skip).limit(limit).all()
            users = [user_model_to_entity(instance) for instance in instances]
            return users

    def find_by_username(self, username: str) -> User | None:
        with self._session_manager() as session:
            instance = session.query(UserModel).filter(UserModel.username == username).first()  # type: ignore
            if instance:
                return user_model_to_entity(instance)
            return None

    def find_by_id(self, id: int) -> User | None:
        instance = self._find_by_id(id)
        return user_model_to_entity(instance)

    def create(self, entity: UserCreate) -> User:
        instance = user_entity_to_model(entity)
        with self._session_manager() as session:
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return user_model_to_entity(instance)

    def update(self, entity: User) -> User:
        with self._session_manager() as session:
            instance_query = session.query(UserModel).filter(UserModel.id == entity.id)
            instance = instance_query.first()
            if not instance:
                raise ValueError("Entity does not exist in database.")
            instance_query.update(entity.__dict__)  # type: ignore
            session.commit()
            session.refresh(instance)
            return user_model_to_entity(instance)

    def delete(self, id: int):
        instance = self._find_by_id(id)
        if not instance:
            raise ValueError(f"Entity does not exist in database.")
        with self._session_manager() as session:
            session.delete(instance)
            session.commit()

    def _find_by_id(self, id: int) -> UserModel | None:
        with self._session_manager() as session:
            return session.query(UserModel).get(id)
