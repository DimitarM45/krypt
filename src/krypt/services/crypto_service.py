from pwdlib import PasswordHash
from os import urandom
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey,
    X25519PublicKey,
)
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from krypt.services.models.crypto_key_pair import CryptoKeyPair
from krypt.services.models.encrypted_payload_dto import EncryptedPayloadDTO
from .abstract_crypto_service import AbstractCryptoService


class CryptoService(AbstractCryptoService):
    def __init__(self, hash_service: PasswordHash) -> None:
        self._hash_service = hash_service

    def generate_key_pair(self) -> CryptoKeyPair:
        private_key: X25519PrivateKey = X25519PrivateKey.generate()

        public_key: X25519PublicKey = private_key.public_key()

        private_bytes: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )

        public_bytes: bytes = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )

        return CryptoKeyPair(private_key=private_bytes, public_key=public_bytes)

    def generate_password_hash(self, password: str) -> str:
        return self._hash_service.hash(password)

    def verify_password_hash(self, plain_password: str, hashed_password: str) -> bool:
        return self._hash_service.verify(plain_password, hashed_password)

    def encrypt_data(self, data: bytes, key: bytes) -> EncryptedPayloadDTO:
        aesgcm: AESGCM = AESGCM(key)

        nonce: bytes = urandom(12)

        encrypted_data: bytes = aesgcm.encrypt(nonce, data, associated_data=None)

        return EncryptedPayloadDTO(encrypted_data, nonce)

    def decrypt_data(self, data: bytes, nonce: bytes, key: bytes) -> bytes:
        aesgcm: AESGCM = AESGCM(key)

        return aesgcm.decrypt(nonce, data, associated_data=None)

    def derive_shared_secret(
        self, private_key_bytes: bytes, peer_public_key_bytes: bytes
    ):
        private_key: X25519PrivateKey = X25519PrivateKey.from_private_bytes(
            private_key_bytes
        )

        peer_public_key: X25519PublicKey = X25519PublicKey.from_public_bytes(
            peer_public_key_bytes
        )

        shared_secret_bytes: bytes = private_key.exchange(peer_public_key)

        hkdf: bytes = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=urandom(32),
            info=b"krypt-websocket-message-key",
        ).derive(shared_secret_bytes)

        return hkdf
