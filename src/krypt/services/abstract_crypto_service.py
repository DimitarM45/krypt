from abc import ABC, abstractmethod
from typing import Any

from krypt.services.models.crypto_key_pair import CryptoKeyPair
from krypt.services.models.encrypted_payload_dto import EncryptedPayloadDTO


class AbstractCryptoService(ABC):
    @abstractmethod
    def generate_key_pair(self) -> CryptoKeyPair:
        pass

    @abstractmethod
    def generate_password_hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify_password_hash(self, plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def encrypt_data(self, data: bytes, key: bytes) -> EncryptedPayloadDTO:
        pass

    @abstractmethod
    def decrypt_data(self, data: bytes, nonce: bytes, key: bytes) -> bytes:
        pass

    @abstractmethod
    def derive_shared_secret(
        self, private_key_bytes: bytes, peer_public_key_bytes: bytes
    ) -> bytes:
        pass
