from src.user.application.user_errors import (
    PaginationError,
    UserAlreadyExistError,
    UserNotFoundError,
)
from src.user.domain.user import User, UserCreate
from src.user.domain.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def find_all(self, limit: int, page: int) -> list[User]:
        if limit <= 0 or limit > 20:
            raise PaginationError("Limit parameter must be between 1 and 20")
        if page < 1:
            raise PaginationError("Page parameter must be greater than 1")

        skip = (page - 1) * limit
        return self.repository.find_all(limit, skip)

    def find_by_username(self, username: str) -> User:
        found_user = self.repository.find_by_username(username)
        if not found_user:
            raise UserNotFoundError(f"Cannot find a user with username={username}")
        return found_user

    def find_by_id(self, id_: int) -> User:
        found_user = self.repository.find_by_id(id_)
        if not found_user:
            raise UserNotFoundError(f"Cannot find a user with id={id}")
        return found_user

    def create(self, user: UserCreate) -> User:
        found_user = self.repository.find_by_username(user.username)
        if found_user:
            raise UserAlreadyExistError(
                f"A user with username={user.username} already exists"
            )
        created_user = self.repository.create(user)
        return created_user

    def update(self, user: User) -> User:
        found_user = self.repository.find_by_id(user.id)
        if not found_user:
            raise UserNotFoundError("User not found")
        updated_user = self.repository.update(user)
        return updated_user

    def delete(self, id_: int) -> None:
        entity = self.find_by_id(id_)
        if not entity:
            raise UserNotFoundError("User not found")
        self.repository.delete(entity)
