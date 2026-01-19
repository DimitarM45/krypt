from krypt.src.dals.abstract_user_repository import AbstractUserRepository
from krypt.src.dals.user_repository import UserRepository

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio.engine import AsyncEngine

def get_user_repository(db_engine: AsyncEngine) -> AbstractUserRepository:
    db_engine.
    
    return UserRepository()
