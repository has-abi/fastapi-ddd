from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.containers import Container
from src.user.application.user_service import UserService
from src.user.domain.user import User, UserCreate

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/id/{user_id}", response_model=User)
@inject
def find_by_id(
    user_id: int, service: UserService = Depends(Provide[Container.user_service])
):
    return service.find_by_id(user_id)


@users_router.get("/page/{page}/offset/{offset}", response_model=list[User])
@inject
def find_all(
    page: int,
    offset: int,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.find_all(offset, page)


@users_router.get("/username/{username}", response_model=User)
@inject
def find_by_username(
    username: str, service: UserService = Depends(Provide[Container.user_service])
):
    return service.find_by_username(username)


@users_router.post("/", response_model=User)
@inject
def create(
    user: UserCreate, service: UserService = Depends(Provide[Container.user_service])
):
    return service.create(user)


@users_router.put("/", response_model=User)
@inject
def update(user: User, service: UserService = Depends(Provide[Container.user_service])):
    return service.update(user)


@users_router.delete("/id/{user_id}")
@inject
def delete(
    user_id: int, service: UserService = Depends(Provide[Container.user_service])
):
    service.delete(user_id)
    return {"message": "User deleted"}
