"""
Loads the auth server .env configuration model.
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

_BASE_PROJECT_DIR: Path = Path(__file__).parent.parent.parent.parent
_ENV_FILE_PATH = _BASE_PROJECT_DIR / ".env"


class Configuration(BaseSettings):
    """
    Pydantic configuration model
    """

    token_signing_secret: str
    access_token_algorithm: str
    access_token_expiration_minutes: int
    db_connection_string: str

    model_config = SettingsConfigDict(env_file=_ENV_FILE_PATH)


config: Configuration = Configuration()
