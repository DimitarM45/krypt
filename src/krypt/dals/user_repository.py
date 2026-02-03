from datetime import datetime
from typing import Any, Optional
from uuid import UUID
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from krypt.dals.abstract_user_repository import AbstractUserRepository
from krypt.dals.models.user import User


class UserRepository(AbstractUserRepository):
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def create_user(self, user: User) -> UUID:
        user.created_at = datetime.now()

        self._db.add(user)

        await self._db.commit()

        return user.id

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        user: Optional[User] = await self._db.get(User, UUID(user_id))

        if user and user.deleted_at:
            return None

        return user

    async def get_user_by_username(self, username: str) -> Optional[User]:
        statement = select(User).where(User.username == username)

        result: Result[Any] = await self._db.execute(statement)

        return result.scalar_one_or_none()

    async def remove_user_by_id(self, user_id: str) -> bool:
        user: Optional[User] = await self._db.get(User, UUID(user_id))

        if not user:
            return False

        user.first_name = None
        user.last_name = None
        user.username = None
        user.public_message_key = None
        user.password_hash = None
        user.email = None
        user.deleted_at = datetime.now()

        await self._db.commit()

        return True

    async def get_password_hash(self, user_id: str) -> Optional[str]:
        statement = select(User.password_hash).where(User.id == user_id)

        result: Result[Any] = await self._db.execute(statement)

        return result.scalar_one_or_none()

    async def user_exists(self, username: str, email: str) -> bool:
        statement = select(User.id).where(User.username == username or User.email == email)

        return (await self._db.execute(statement)).first() is not None
