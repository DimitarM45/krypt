from fastapi import Depends
from krypt.services.abstract_auth_service import AbstractAuthService
from pwdlib import PasswordHash
from krypt.auth_server.dependencies.repositories import get_user_repository
from krypt.configuration import Configuration, get_config
from krypt.services.abstract_crypto_service import AbstractCryptoService
from krypt.services.abstract_user_service import AbstractUserService
from krypt.services.auth_service import AuthService
from krypt.services.crypto_service import CryptoService
from krypt.services.user_service import UserService
from krypt.dals.abstract_user_repository import AbstractUserRepository


hash_service: PasswordHash = PasswordHash.recommended()


def get_hash_service() -> PasswordHash:
    return hash_service


def get_crypto_service(
    hash_service: PasswordHash = Depends(get_hash_service),
) -> AbstractCryptoService:
    return CryptoService(hash_service)


def get_auth_service(
    crypto_service: AbstractCryptoService = Depends(get_crypto_service),
    config: Configuration = Depends(get_config),
) -> AbstractAuthService:
    return AuthService(crypto_service, config)


def get_user_service(
    user_repo: AbstractUserRepository = Depends(get_user_repository),
    auth_service: AbstractAuthService = Depends(get_auth_service),
    crypto_service: AbstractCryptoService = Depends(get_crypto_service),
) -> AbstractUserService:
    return UserService(user_repo, auth_service, crypto_service)
