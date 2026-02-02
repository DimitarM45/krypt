from pydantic import BaseModel, ConfigDict

class AuthUserDTO(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: str
    username: str
    password_hash: str