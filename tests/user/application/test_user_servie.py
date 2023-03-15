from datetime import date
from unittest.mock import MagicMock

import pytest

from src.user.application.user_errors import (
    PaginationError,
    UserAlreadyExistError,
    UserNotFoundError,
)
from src.user.domain.user import User
from src.user.domain.user_repository import UserRepository


class TestUserService:
    def test_find_all_basic(self, app):
        mock_repository = MagicMock(spec=UserRepository)
        test_users = [
            User(
                id=1,
                username="john-b",
                first_name="John",
                last_name="Ben",
                birth_date=date(2001, 3, 4),
                gender="male",
            ),
            User(
                id=2,
                username="monica",
                first_name="Monica",
                last_name="Astrid",
                birth_date=date(2001, 5, 4),
                gender="female",
            ),
        ]
        mock_repository.find_all.return_value = test_users
        page, limit = 1, 10
        with app.container.user_repository.override(mock_repository):
            results = app.container.user_service().find_all(limit, page)
        assert results == test_users

    def test_find_all_raises_pagination_error_on_page_less_than_one(self, app):
        with pytest.raises(PaginationError):
            app.container.user_service().find_all(limit=10, page=0)

    def test_find_all_raises_pagination_error_on_negative_limit(self, app):
        with pytest.raises(PaginationError):
            app.container.user_service().find_all(limit=-1, page=1)

    def test_find_all_raises_pagination_error_on_limit_greater_than_20(self, app):
        with pytest.raises(PaginationError):
            app.container.user_service().find_all(limit=21, page=1)

    def test_find_by_username_basic(self, app, random_user):
        mock_repository = MagicMock(spec=UserRepository)
        mock_repository.find_by_username.return_value = random_user
        with app.container.user_repository.override(mock_repository):
            found_user = app.container.user_service().find_by_username("john")
        assert found_user == random_user

    def test_find_by_username_raises_user_not_found_error(self, app):
        mock_repository = MagicMock(spec=UserRepository)
        mock_repository.find_by_username.return_value = None
        with app.container.user_repository.override(mock_repository):
            with pytest.raises(UserNotFoundError):
                app.container.user_service().find_by_username("john")

    def test_find_by_id_basic(self, app, random_user):
        mock_repository = MagicMock(spec=UserRepository)
        mock_repository.find_by_id.return_value = random_user
        with app.container.user_repository.override(mock_repository):
            found_user = app.container.user_service().find_by_id(1)
        assert found_user == random_user

    def test_find_by_id_raises_user_not_found_error(self, app):
        mock_repository = MagicMock(spec=UserRepository)
        mock_repository.find_by_id.return_value = None
        with app.container.user_repository.override(mock_repository):
            with pytest.raises(UserNotFoundError):
                app.container.user_service().find_by_id(1)

    def test_create_basic(self, app, random_user, random_user_create):
        mock_repository = MagicMock(spec=UserRepository)

        mock_repository.find_by_username.return_value = None
        mock_repository.create.return_value = random_user
        with app.container.user_repository.override(mock_repository):
            created_user = app.container.user_service().create(random_user_create)
        assert created_user == random_user

    def test_create_raises_user_already_exists_error(
        self, app, random_user, random_user_create
    ):
        mock_repository = MagicMock(spec=UserRepository)
        mock_repository.find_by_username.return_value = random_user
        with app.container.user_repository.override(mock_repository):
            with pytest.raises(UserAlreadyExistError):
                app.container.user_service().create(random_user_create)
