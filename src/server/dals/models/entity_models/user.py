"""
Docstring for krypt.src.server.dals.models.entity_models.user
"""

from datetime import datetime
import uuid

from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped, mapped_column

from krypt.src.server.dals.models.entity_models.base import Base


class User(Base):
    """
    The User model.
    """

    __tablename__ = "Users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[str] = mapped_column(String(50))
    profile_pic_url: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[datetime] = mapped_column(DateTime())
