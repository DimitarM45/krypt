from pydantic import BaseModel


class CryptoKeyPair(BaseModel):
    public_key: 