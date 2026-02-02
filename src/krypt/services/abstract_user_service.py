from typing import Optional
from abc import ABC, abstractmethod

from krypt.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.services.models.user_dto import UserDTO
from krypt.services.models.auth_user_dto import AuthUserDTO

class AbstractUserService(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[UserDTO]:
        pass

    @abstractmethod
    async def create_user(self, user_data: RegisterUserRequest) -> Optional[str]:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[UserDTO]:
        pass

    @abstractmethod
    async def delete_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    async def get_auth_user(self, username: str) -> Optional[AuthUserDTO]:
        pass