from dataclasses import dataclass


@dataclass
class CryptoKeyPair:
    public_key: bytes
    private_key: bytes
