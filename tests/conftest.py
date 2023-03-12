import pytest
from fastapi.testclient import TestClient

from src.app import create_app

app = create_app()


@pytest.fixture
def client():
    yield TestClient(app)
