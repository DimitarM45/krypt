"""
Contains the main implementation of the AbstractUserService.
"""

from typing import Optional
from fastapi import Depends

from krypt.auth_server.dependencies.repositories import get_user_repository
from krypt.auth_server.routers.auth.models.register_user_request import RegisterUserRequest
from krypt.auth_server.services.abstract_user_service import AbstractUserService
from krypt.auth_server.services.models.user_dto import UserDTO
from krypt.dals.abstract_user_repository import AbstractUserRepository
from krypt.dals.models.user import User

class UserService(AbstractUserService):
    """
    Main implementation of the AbstractUserService.
    """

    def __init__(
        self, user_repository: AbstractUserRepository = Depends(get_user_repository)
    ) -> None:
        self._user_repository: AbstractUserRepository = user_repository

    async def get_user_by_id(self, user_id: str) -> Optional[UserDTO]:
        user: Optional[User] = await self._user_repository.get_user_by_id(user_id)

        if not user:
            return None

        return UserDTO(
            first_name=user.first_name, last_name=user.last_name, username=user.username
        )

    async def create_user(self, user_data: RegisterUserRequest) -> Optional[str]:
        return str(await self._user_repository.create_user(user_data))
