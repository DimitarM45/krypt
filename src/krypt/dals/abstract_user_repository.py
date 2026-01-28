from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from krypt.auth_server.routers.auth.models.register_user_request import RegisterUserRequest
from krypt.dals.models.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: RegisterUserRequest) -> UUID:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    async def remove_user_by_id(self, user_id: str) -> bool:
        pass