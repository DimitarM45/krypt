from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from krypt.dals.user_repository import UserRepository
from krypt.auth_server.dependencies.database import get_db_context
from krypt.dals.abstract_user_repository import AbstractUserRepository


def get_user_repository(
    db_context: AsyncSession = Depends(get_db_context),
) -> AbstractUserRepository:
    return UserRepository(db_context)
