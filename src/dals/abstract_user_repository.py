from abc import ABC, abstractmethod

from auth_server.routers.auth.models.register_user_request import RegisterUserRequest


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: RegisterUserRequest) -> bool:
        pass

    @abstractmethod
    async def get_user_by_id(self, id: str) -> User:
        Bas