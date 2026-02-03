from pydantic import BaseModel, EmailStr, Field, SecretStr, field_validator

from krypt.auth_server.routers.auth.models.validation_constants import (
    EMAIL_MAX_LENGTH,
    FIRST_NAME_MAX_LENGTH,
    LAST_NAME_MAX_LENGTH,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    USERNAME_MAX_LENGTH,
)


class RegisterUserRequest(BaseModel):
    first_name: str = Field(max_length=FIRST_NAME_MAX_LENGTH)
    last_name: str = Field(max_length=LAST_NAME_MAX_LENGTH)
    username: str = Field(max_length=USERNAME_MAX_LENGTH)
    public_message_key: str = Field()
    email: EmailStr = Field(max_length=EMAIL_MAX_LENGTH)
    password: SecretStr = Field(
        min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )

    @classmethod
    @field_validator("password")
    def validate_password(cls, value: SecretStr) -> SecretStr:
        """
        Validates the input password
        """
        password: str = value.get_secret_value()

        if not isinstance(password, str):
            raise TypeError("Password must be a string!")
        if not any(char.isdigit() for char in password):
            raise ValueError("Passoword must contain at least one digit!")
        if all(char.isalnum() for char in password):
            raise ValueError("Password must contain at least one special character!")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter!")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter!")

        return value
