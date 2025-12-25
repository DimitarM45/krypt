"""
Contains the main abstract class that denotes the traffic of data between a client and a server.
"""

from abc import ABC, abstractmethod


class TransportService(ABC):
    """
    An abstract class that provides an interface for sending data 
    between a client instance and a server instance, and vice versa.
    """

    @abstractmethod
    async def send_data(self, data: bytes) -> None:
        """
        An abstract method that provdies an interface for sending data.

        :param data: The data being sent.
        :type data: bytes
        """

    @abstractmethod
    async def receive_data(self) -> bytes:
        """
        An abstract method that provides an interface for data reception.
        """
