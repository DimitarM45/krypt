from pydantic import BaseModel, ConfigDict, field_validator


class AuthUserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    username: str
    password_hash: str

    @field_validator("id", mode="before")
    @classmethod
    def uuid_to_str(cls, value):
        return str(value)
