"""
The abstract user repository class for managing user entities.
"""

from typing import Optional
import uuid

from abc import ABC, abstractmethod

from krypt.src.server.dals.models.entity_models.user import User
from krypt.src.server.dals.models.request_models.create_user_request import (
    CreateUserRequest,
)


class UserRepository(ABC):
    """
    An abstract class for CRUD operations with users
    """

    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Get a user by their username.

        :param username: Username of the user
        :type username: str
        :return: User entity model
        :rtype: User
        """

    @abstractmethod
    async def get_user_by_id(self, id: uuid.UUID) -> Optional[User]:
        """
        Get a user by their username.

        :param id: The id of the user
        :type id: str
        :return: User entity model
        :rtype: User
        """

    @abstractmethod
    async def create_user(self, create_user_request: CreateUserRequest) -> Optional[str]:
        """
        Create a new user.

        :param self: The id of the user
        :param create_user_request: The data for the new user
        :type create_user_request: CreateUserRequest
        :return: The id of the newly created user if successful, otherwise None.
        :rtype: str
        """

    @abstractmethod
    async def remove_user(self, id: uuid.UUID) -> bool:
        """
        Remove a user.

        :param id: The id of the user
        :type id: str
        :return: Whether the operation was successful.
        :rtype: bool
        """
