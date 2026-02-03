from dataclasses import dataclass


@dataclass
class EncryptedPayloadDTO:
    data: bytes
    nonce: bytes
