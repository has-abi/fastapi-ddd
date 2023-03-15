from datetime import date

import pytest
from fastapi.testclient import TestClient

from src.app import create_app
from src.user.domain.user import User, UserCreate


@pytest.fixture
def app():
    test_app = create_app()
    yield test_app


@pytest.fixture
def client(app):
    return TestClient(app)


@pytest.fixture
def random_user():
    return User(
        id=1,
        username="john",
        first_name="John",
        last_name="Doe",
        birth_date=date(2004, 11, 12),
        gender="male",
    )


@pytest.fixture
def random_user_create():
    return UserCreate(
        username="john",
        first_name="John",
        last_name="Doe",
        birth_date=date(2004, 11, 12),
        gender="male",
    )
