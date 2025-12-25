"""
Contains the main abstract class that denotes encryption and decryption of data.
"""

from abc import ABC, abstractmethod

from .strategies.cryptography_strategy import CryptographyStrategy


class CryptographyService(ABC):
    """
    An abstract class that provides an interface for data encryption and decryption.
    """

    @abstractmethod
    def encrypt_data(self, strategy: CryptographyStrategy, data: bytes) -> bytes:
        """
        Docstring for encrypt_data

        :param self: Description
        :param data: Description
        :type data: bytes
        :return: Description
        :rtype: bytes
        """

    @abstractmethod
    def decrypt_data(self, strategy: CryptographyStrategy, data: bytes) -> bytes:
        """
        Docstring for decrypt_data

        :param self: Description
        :param data: Description
        :type data: bytes
        :return: Description
        :rtype: bytes
        """
