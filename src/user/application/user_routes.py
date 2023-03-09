from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Response

from src.containers import Container
from src.user.application.user_service import UserService
from src.user.domain.user import User, UserCreate

users_router = APIRouter(prefix="/users")


@users_router.get("/id/{id}")
@inject
def find_by_id(
    id: int, service: UserService = Depends(Provide[Container.user_service])
):
    return service.find_by_id(id)


@users_router.get("/page/{page}/offset/{offset}", response_model=list[User])
@inject
def find_all(
    page: int,
    offset: int,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.find_all(offset, page)


@users_router.get("/username/{username}")
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
    found_user = service.find_by_username(user.username)
    if found_user:
        raise HTTPException(status_code=400, detail="username already exist")
    return service.create(user)


@users_router.put("/", response_model=User)
@inject
def update(user: User, service: UserService = Depends(Provide[Container.user_service])):
    found_user = service.find_by_id(user.id)
    if not found_user:
        raise HTTPException(status_code=404, detail="User does not exist")
    return service.update(user)


@users_router.delete("/id/{id}")
@inject
def delete(id: int, service: UserService = Depends(Provide[Container.user_service])):
    found_user = service.find_by_id(id)
    if not found_user:
        raise HTTPException(status_code=404, detail="User does not exist")
    service.delete(id)
    return {"mesage": "user deleted"}
