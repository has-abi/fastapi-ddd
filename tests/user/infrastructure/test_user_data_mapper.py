from datetime import date
from unittest.mock import MagicMock

from src.user.domain.user import User, UserCreate
from src.user.infrastructure.user_data_mapper import (
    user_entity_to_model,
    user_model_to_entity,
)


class TestUserDataMapper:
    def test_user_model_to_entity_should_convert_user_model_to_entity(self):
        mock_user_model = MagicMock(
            id=1,
            username="ah-med",
            first_name="Ahmed",
            last_name="Hamdi",
            birth_date=date(2000, 2, 2),
            gender="male",
        )
        user_entity = user_model_to_entity(mock_user_model)
        assert user_entity.id == 1
        assert user_entity.username == "ah-med"
        assert user_entity.first_name == "Ahmed"
        assert user_entity.last_name == "Hamdi"
        assert user_entity.birth_date == date(2000, 2, 2)
        assert user_entity.gender == "male"

    def test_user_entity_to_model_should_convert_user_entity_to_model(self):
        user_entity = User(
            id=1,
            username="malik",
            first_name="malik",
            last_name="evona",
            birth_date=date(1995, 5, 15),
            gender="male",
        )
        user_model = user_entity_to_model(user_entity)
        assert user_model.id == 1
        assert user_model.username == "malik"
        assert user_model.first_name == "malik"
        assert user_model.last_name == "evona"
        assert user_model.birth_date == date(1995, 5, 15)
        assert user_model.gender == "male"

    def test_user_entity_to_model_should_convert_user_entity_to_model_for_user_create(
        self,
    ):
        user_create = UserCreate(
            username="malik",
            first_name="malik",
            last_name="evona",
            birth_date=date(1995, 5, 15),
            gender="male",
        )
        user_model = user_entity_to_model(user_create)
        assert user_model.id == None
        assert user_model.username == "malik"
        assert user_model.first_name == "malik"
        assert user_model.last_name == "evona"
        assert user_model.birth_date == date(1995, 5, 15)
        assert user_model.gender == "male"
