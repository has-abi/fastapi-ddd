from src.user.domain.user import User, UserCreate
from src.user.infrastructure.user_model import UserModel


def user_model_to_entity(instance: UserModel) -> User:
    return User(
        id=instance.id,  # type: ignore
        username=instance.username,  # type: ignore
        first_name=instance.first_name,  # type: ignore
        last_name=instance.last_name,  # type: ignore
        birth_date=instance.birth_date,  # type: ignore
        gender=instance.gender,  # type: ignore
    )


def user_entity_to_model(user: User | UserCreate) -> UserModel:
    user_model = UserModel(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        birth_date=user.birth_date,
        gender=user.gender,
    )
    if isinstance(user, User):
        user_model.id = user.id  # type: ignore
    return user_model
