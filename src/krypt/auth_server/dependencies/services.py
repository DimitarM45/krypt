from fastapi import Depends
from pwdlib import PasswordHash
from krypt.auth_server.dependencies.repositories import get_user_repository
from krypt.configuration import Configuration
from krypt.services.auth_service import AuthService
from krypt.services.user_service import UserService
from krypt.dals.abstract_user_repository import AbstractUserRepository


def get_user_service(
    user_repo: AbstractUserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repo)


def get_auth_service(
    hash_service: PasswordHash = Depends(PasswordHash.recommended),
    config: Configuration = Depends(Configuration)
) -> AuthService:
    return AuthService(hash_service, config)
