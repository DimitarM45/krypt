from abc import ABC, abstractmethod

from krypt.auth_server.routers.auth.models.register_user_request import RegisterUserRequest
from krypt.dals.models.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: RegisterUserRequest) -> str:
        pass

    @abstractmethod
    async def get_user_by_id(self, id: str) -> User:
        pass