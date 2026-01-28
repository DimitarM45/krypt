from dataclasses import dataclass

from pydantic import BaseModel, SecretStr, Field

from krypt.auth_server.routers.auth.models.validation_constants import (
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    USERNAME_MAX_LENGTH,
)


@dataclass
class LoginUserRequest(BaseModel):
    username: str = Field(max_length=USERNAME_MAX_LENGTH)
    password: SecretStr = Field(
        min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )
