from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from krypt.dals.models.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> UUID:
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

    @abstractmethod
    async def user_exists(self, username: str) -> bool:
        pass
