from abc import ABC, abstractmethod
from typing import Any


class AbstractCryptoService(ABC):
    @abstractmethod
    def generate_asymmetric_key_pair(self):
        pass

    @abstractmethod
    def generate_symmetric_key(self):
        pass

    @abstractmethod
    def generate_password_hash(self, password: str, salt: bytes) -> str:
        pass

    @abstractmethod
    def verify_password_hash(self, plain_password: str, hashed_password: str) -> bool:
        pass
