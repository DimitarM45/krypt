from krypt.auth_server.routers.auth.models.register_user_request import RegisterUserRequest
from krypt.dals.abstract_user_repository import AbstractUserRepository
from krypt.dals.models.user import User

from sqlalchemy.orm import Session

class UserRepository(AbstractUserRepository):
    def __init__(self, db: Session) -> None:
        self._db = db

    async def create_user(self, user_data: RegisterUserRequest) -> str:
        raise NotImplementedError

    async def get_user_by_id(self, id: str) -> User:
        raise NotImplementedError
