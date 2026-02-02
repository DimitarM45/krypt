from typing import Optional
import uuid
from sqlalchemy import String, UUID, text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )

    first_name: Mapped[Optional[str]] = mapped_column(String(30))
    last_name: Mapped[Optional[str]] = mapped_column(String(30))
    username: Mapped[Optional[str]] = mapped_column(String(30), unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(100))
    password_salt: Mapped[Optional[str]] = mapped_column(String(100))
    public_message_key: Mapped[Optional[str]] = mapped_column()
