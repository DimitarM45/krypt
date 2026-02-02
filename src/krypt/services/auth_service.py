from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from krypt.auth_server.routers.auth.models.token import Token
from krypt.configuration import Configuration
from . import AbstractAuthService


class AuthService(AbstractAuthService):
    def __init__(
        self,
        hash_service: PasswordHash,
        config: Configuration,
    ) -> None:
        self._hash_service: PasswordHash = hash_service
        self._config = config

    def create_access_token(
        self, data: dict, expires_delta: timedelta, token_type: str
    ) -> Token:
        jwt_data = data.copy()

        expiration_date: datetime = datetime.now(timezone.utc) + expires_delta

        jwt_data.update({"exp": expiration_date})

        encoded_token: str = jwt.encode(
            jwt_data,
            self._config.token_signing_secret,
            algorithm=self._config.access_token_algorithm,
        )

        return Token(access_token=encoded_token, token_type=token_type)

    def get_password_hash(self, password: str) -> str:
        return self._hash_service.hash(password)

    def verify_password_hash(self, plain_password: str, hashed_password: str) -> bool:
        return self._hash_service.verify(plain_password, hashed_password)
