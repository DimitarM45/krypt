from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException

from krypt.auth_server.dependencies.services import get_user_service
from krypt.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.auth_server.services.abstract_user_service import AbstractUserService


auth_router: APIRouter = APIRouter()

UserServiceDependency = Annotated[AbstractUserService, Depends(get_user_service)]


@auth_router.post("/register", status_code=201)
async def register_user(
    request: RegisterUserRequest,
    user_service: UserServiceDependency,
):
    user_id: Optional[str] = await user_service.create_user(request)

    if not user_id:
        raise HTTPException(409, "User could not be created!")

    return user_id


# @auth_router.post("/login", status_code=201)
# async def login_user(
#     request: LoginUserRequest
# ):
#     pass


@auth_router.post("/logout")
async def logout_user():
    pass


@auth_router.post("/register")
def create_user():
    pass
