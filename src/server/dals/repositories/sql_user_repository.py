"""
An implementation of the abstract UserRepository class that communicates with an SQL server.
"""

from uuid import UUID
from krypt.src.server.dals.repositories.user_repository import UserRepository

from krypt.src.server.dals.models.entity_models.user import User

from krypt.src.server.dals.models.request_models.create_user_request import CreateUserRequest


class SqlUserRepository(UserRepository):
    """
    An implementation of the abstract UserRepository class that communicates with an SQL server.
    """
    async def get_user_by_username(self, username: str) -> User | None:
        raise NotImplementedError

    async def get_user_by_id(self, id: UUID) -> User | None:
        raise NotImplementedError

    async def create_user(self, create_user_request: CreateUserRequest) -> str | None:
        raise NotImplementedError

    async def remove_user(self, id: UUID) -> bool:
        raise NotImplementedError
