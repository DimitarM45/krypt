from abc import ABC, abstractmethod
from datetime import timedelta

from krypt.auth_server.routers.auth.models.token import Token


class AbstractAuthService(ABC):
    @abstractmethod
    def create_access_token(
        self, data: dict, expires_delta: timedelta, token_type: str
    ) -> Token:
        pass
