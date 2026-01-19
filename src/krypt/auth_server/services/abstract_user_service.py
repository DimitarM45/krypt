from typing import Optional
from abc import ABC, abstractmethod

from krypt.src.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.src.auth_server.services.models.user_dto import UserDTO


class AbstractUserService(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[UserDTO]:
        pass

    @abstractmethod
    async def create_user(self, user_data: RegisterUserRequest) -> Optional[str]:
        pass
