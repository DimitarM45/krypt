from typing import Any

from pwdlib import PasswordHash
from .abstract_crypto_service import AbstractCryptoService


class CryptoService(AbstractCryptoService):
    def __init__(self, hash_service: PasswordHash) -> None:
        self._hash_service = hash_service

    def generate_asymmetric_key_pair(self):
        raise NotImplementedError

    def generate_symmetric_key(self):
        raise NotImplementedError

    def generate_password_hash(self, password: str, salt: bytes) -> str:
        return self._hash_service.hash(password, salt=salt)

    def verify_password_hash(self, plain_password: str, hashed_password: str) -> bool:
        return self._hash_service.verify(plain_password, hashed_password)
