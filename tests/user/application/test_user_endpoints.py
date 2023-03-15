from datetime import date
from unittest.mock import MagicMock

from src.user.application.user_service import UserService
from src.user.domain.user import User

USERS_BASE_URL = "/api/users"


class TestUserEndpoints:
    def test_find_all(self, app, client):
        mock_service = MagicMock(spec=UserService)
        mock_service.find_all.return_value = [
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
        with app.container.user_service.override(mock_service):
            response = client.get(f"{USERS_BASE_URL}/page/1/offset/10")
        assert response.status_code == 200
        data = response.json()
        assert data == [
            {
                "id": 1,
                "username": "john-b",
                "first_name": "John",
                "last_name": "Ben",
                "birth_date": "2001-03-04",
                "gender": "male",
            },
            {
                "id": 2,
                "username": "monica",
                "first_name": "Monica",
                "last_name": "Astrid",
                "birth_date": "2001-05-04",
                "gender": "female",
            },
        ]

    def test_find_by_id(self, app, client, random_user):
        mock_service = MagicMock(spec=UserService)
        mock_service.find_by_id.return_value = random_user
        with app.container.user_service.override(mock_service):
            response = client.get(f"{USERS_BASE_URL}/id/1")
        assert response.status_code == 200
        data = response.json()
        assert data == {
            "id": 1,
            "username": "john",
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "2004-11-12",
            "gender": "male",
        }

    def test_find_by_username(self, app, client, random_user):
        mock_service = MagicMock(spec=UserService)
        mock_service.find_by_username.return_value = random_user
        with app.container.user_service.override(mock_service):
            response = client.get(f"{USERS_BASE_URL}/username/john")
        assert response.status_code == 200
        data = response.json()
        assert data == {
            "id": 1,
            "username": "john",
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "2004-11-12",
            "gender": "male",
        }

    def test_create_user(self, app, client, random_user):
        mock_service = MagicMock(spec=UserService)
        mock_service.create.return_value = random_user
        user_to_create = {
            "username": "john",
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "2004-11-12",
            "gender": "male",
        }
        with app.container.user_service.override(mock_service):
            response = client.post(f"{USERS_BASE_URL}/", json=user_to_create)
        user_to_create["id"] = 1  # type: ignore
        assert response.status_code == 200
        data = response.json()
        assert data == user_to_create

    def test_update_user(self, app, client, random_user):
        mock_service = MagicMock(spec=UserService)
        mock_service.update.return_value = random_user
        user_to_update = {
            "id": 1,
            "username": "john",
            "first_name": "John",
            "last_name": "Arina",
            "birth_date": "2004-11-12",
            "gender": "male",
        }
        with app.container.user_service.override(mock_service):
            response = client.put(f"{USERS_BASE_URL}/", json=user_to_update)
        user_to_update["last_name"] = "Doe"
        assert response.status_code == 200
        data = response.json()
        assert data == user_to_update

    def test_delete_user(self, app, client):
        mock_service = MagicMock(spec=UserService)
        mock_service.delete = MagicMock(return_value=True)
        with app.container.user_service.override(mock_service):
            response = client.delete(f"{USERS_BASE_URL}/id/1")
        assert response.status_code == 200
        assert response.json() == {"message": "User deleted"}
