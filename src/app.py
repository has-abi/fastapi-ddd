from fastapi import FastAPI

from src.containers import Container
from src.user.application.user_routes import users_router


def create_app() -> FastAPI:
    app = FastAPI()

    container = Container()
    app.container = container  # type: ignore

    app.include_router(users_router, prefix="/api")
    return app
