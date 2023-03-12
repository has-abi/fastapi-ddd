from dependency_injector import containers, providers

from src.database import Database
from src.settings import Settings
from src.user.application.user_service import UserService
from src.user.infrastructure.sqlalchemy_user_repository import SQLAlchemyUserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["src.user.application.user_routes"]
    )

    settings = providers.Configuration()
    settings.from_pydantic(Settings())

    db = providers.Singleton(Database)

    user_repository = providers.Factory(
        SQLAlchemyUserRepository,
        session_manager=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        repository=user_repository,
    )
