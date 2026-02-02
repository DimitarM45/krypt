from pydantic import BaseModel, SecretStr, Field

from krypt.auth_server.routers.auth.models.validation_constants import (
    USERNAME_MAX_LENGTH,
)


class LoginUserRequest(BaseModel):
    username: str = Field(max_length=USERNAME_MAX_LENGTH)
    password: SecretStr = Field()
