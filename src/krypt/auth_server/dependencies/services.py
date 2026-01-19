from fastapi import Depends
from krypt.auth_server.dependencies.repositories import get_user_repository
from krypt.auth_server.services.user_service import UserService
from krypt.dals.abstract_user_repository import AbstractUserRepository


def get_user_service(
    repo: AbstractUserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)
