from pydantic import BaseModel, ConfigDict


class UserDTO(BaseModel):
    """
    Docstring
    """

    model_config = ConfigDict(from_attributes=True)

    id: str
    first_name: str
    last_name: str
    username: str
    public_message_key: str
