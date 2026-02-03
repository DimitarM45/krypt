from typing import Optional
import uuid
from sqlalchemy import String, UUID, text
from sqlalchemy.orm import Mapped, mapped_column

from krypt.auth_server.routers.auth.models.validation_constants import EMAIL_MAX_LENGTH, FIRST_NAME_MAX_LENGTH, LAST_NAME_MAX_LENGTH, USERNAME_MAX_LENGTH

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )

    first_name: Mapped[Optional[str]] = mapped_column(String(FIRST_NAME_MAX_LENGTH))
    last_name: Mapped[Optional[str]] = mapped_column(String(LAST_NAME_MAX_LENGTH))
    username: Mapped[Optional[str]] = mapped_column(String(USERNAME_MAX_LENGTH), unique=True)
    email: Mapped[Optional[str]] = mapped_column(String(EMAIL_MAX_LENGTH), unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(100))
    public_message_key: Mapped[Optional[str]] = mapped_column(String())
