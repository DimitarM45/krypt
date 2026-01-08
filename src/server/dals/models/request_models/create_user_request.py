"""
DTO for passing arguments to the ..user_repository
"""

from dataclasses import dataclass

from datetime import datetime


@dataclass
class CreateUserRequest:
    """
    DTO for passing arguments to the ..user_repository
    """

    username: str
    email: str
    password_hash: str
    profile_pic_url: str
    date_of_birth: datetime
