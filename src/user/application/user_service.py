from src.user.domain.user import User, UserCreate
from src.user.domain.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def find_all(self, limit: int, page: int) -> list[User]:
        if limit <= 0 or limit > 20:
            raise ValueError("Limit parameter must be between 1 and 20")
        if page <= 0:
            raise ValueError("Page parameter must be greater than 0")

        skip = (page - 1) * limit
        return self.repository.find_all(limit, skip)

    def find_by_username(self, username: str) -> User | None:
        found_user = self.repository.find_by_username(username)
        return found_user

    def find_by_id(self, id: int) -> User | None:
        found_user = self.repository.find_by_id(id)
        return found_user

    def create(self, user: UserCreate) -> User:
        created_user = self.repository.create(user)
        return created_user

    def update(self, user: User) -> User:
        updated_user = self.repository.update(user)
        return updated_user

    def delete(self, id: int) -> None:
        self.repository.delete(id)
