from krypt.src.auth_server.routers.auth.models.register_user_request import RegisterUserRequest
from krypt.src.dals.abstract_user_repository import AbstractUserRepository
from krypt.src.dals.models.user import User

from sqlalchemy.orm import Session

class UserRepository(AbstractUserRepository):
    def __init__(self, db: Session) -> None:
        self._db = db

    async def create_user(self, user_data: RegisterUserRequest) -> str:
        query = insert(user_table)

    async def get_user_by_id(self, id: str) -> User:
        raise NotImplementedError
