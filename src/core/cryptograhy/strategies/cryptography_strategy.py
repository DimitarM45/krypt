"""
Contains the main abstract class that denotes the encryption/decryption strategy.
"""

from abc import ABC, abstractmethod

class CryptographyStrategy(ABC):
    """
    An abstract class that provides an interface for the encryption and decryption strategy.
    """

    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        """
        Docstring for encrypt
        
        :param self: Description
        :param data: Description
        :type data: bytes
        :return: Description
        :rtype: bytes
        """

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes:
        """
        Docstring for decrypt
        
        :param self: Description
        :param data: Description
        :type data: bytes
        :return: Description
        :rtype: bytes
        """
       