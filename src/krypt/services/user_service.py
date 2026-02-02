"""
Contains the main implementation of the AbstractUserService.
"""

from typing import Optional

from krypt.services.abstract_auth_service import AbstractAuthService
from krypt.services.auth_service import AuthService
from krypt.services.models.auth_user_dto import AuthUserDTO
from krypt.services.models.user_dto import UserDTO
from krypt.services.abstract_user_service import AbstractUserService

from krypt.dals.models.user import User
from krypt.dals.abstract_user_repository import AbstractUserRepository

from krypt.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.utils.pydantic_mapping import db_model_to_dto


class UserService(AbstractUserService):
    """
    Main implementation of the AbstractUserService.
    """

    def __init__(self, user_repository: AbstractUserRepository, auth_service: AbstractAuthService) -> None:
        self._user_repository: AbstractUserRepository = user_repository

    async def get_user_by_id(self, user_id: str) -> Optional[UserDTO]:
        user: Optional[User] = await self._user_repository.get_user_by_id(user_id)

        if not user or user.deleted_at:
            return None

        return db_model_to_dto(user, UserDTO)

    async def create_user(self, user_data: RegisterUserRequest) -> Optional[str]:
        if self._user_repository.user_exists(user_data.username):
            return None

        user: User = User()
        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.username = user_data.username

        

        return str(await self._user_repository.create_user())

    async def get_user_by_username(self, username: str) -> Optional[UserDTO]:
        user: Optional[User] = await self._user_repository.get_user_by_username(
            username
        )

        if not user or user.deleted_at:
            return None

        return db_model_to_dto(user, UserDTO)

    async def delete_user(self, user_id: str) -> bool:
        return await self._user_repository.remove_user_by_id(user_id)

    async def get_auth_user(self, username: str) -> Optional[AuthUserDTO]:
        user: Optional[User] = await self._user_repository.get_user_by_username(username)

        if not user or user.deleted_at:
            return None

        return db_model_to_dto(user, AuthUserDTO)
