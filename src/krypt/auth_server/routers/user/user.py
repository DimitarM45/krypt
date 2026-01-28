from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException
from krypt.auth_server.dependencies.services import get_user_service
from krypt.auth_server.services.abstract_user_service import AbstractUserService
from krypt.auth_server.services.models.user_dto import UserDTO
from krypt.auth_server.services.user_service import UserService

user_router: APIRouter = APIRouter()

UserServiceDependency = Annotated[AbstractUserService, Depends(get_user_service)]

@user_router.get('/{user_id}', status_code=200)
async def get_user(user_id: str, user_service: UserServiceDependency):
    user: Optional[UserDTO] = await user_service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(404)

    return user

@user_router.delete('/')
async def delete_user(user_id: str, user_service: UserServiceDependency):
    

