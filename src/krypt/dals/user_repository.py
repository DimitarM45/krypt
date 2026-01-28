from datetime import datetime
from typing import Any, Optional
from uuid import UUID
from sqlalchemy import Result, select 
from sqlalchemy.ext.asyncio import AsyncSession

from krypt.auth_server.routers.auth.models.register_user_request import (
    RegisterUserRequest,
)
from krypt.dals.abstract_user_repository import AbstractUserRepository
from krypt.dals.models.user import User


class UserRepository(AbstractUserRepository):
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def create_user(self, user_data: RegisterUserRequest) -> UUID:
        new_user: User = User()

        new_user.was_created = datetime.now()
        new_user.first_name = user_data.first_name
        new_user.last_name = user_data.last_name
        new_user.username = user_data.username
        new_user.public_message_key = user_data.public_message_key

        self._db.add(new_user)

        await self._db.commit()

        return new_user.id

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        user: Optional[User] = await self._db.get(User, UUID(user_id))

        if user and user.was_deleted:
            return None

        return user

    async def get_user_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)

        result: Result[Any] = await self._db.execute(statement)

        return result.scalar_one_or_none()

    async def remove_user_by_id(self, user_id: str) -> bool:
        user: Optional[User] = await self._db.get(User, UUID(user_id))

        if not user:
            return False

        user.first_name = None,
        user.last_name = None,
        user.username = None,
        user.public_message_key = None,
        user.was_deleted = datetime.now()

        await self._db.commit()

        return True
