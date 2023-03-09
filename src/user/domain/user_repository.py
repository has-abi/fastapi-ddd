from abc import abstractmethod

from src.user.domain.user import User, UserCreate


class UserRepository:
    @abstractmethod
    def find_all(self, limit: int, skip: int) -> list[User]:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> User | None:
        pass

    @abstractmethod
    def create(self, entity: UserCreate) -> User:
        pass

    @abstractmethod
    def update(self, entity: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
