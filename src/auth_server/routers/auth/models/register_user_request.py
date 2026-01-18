from dataclasses import dataclass

from pydantic import BaseModel, EmailStr, Field, SecretStr, field_validator


@dataclass
class RegisterUserRequest(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    username: str = Field(max_length=100)
    email: EmailStr
    password: SecretStr = Field(min_length=8, max_length=100)

    @field_validator("password")
    @classmethod
    def validate_password(
        cls: type["RegisterUserRequest"], value: SecretStr
    ) -> SecretStr:
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
