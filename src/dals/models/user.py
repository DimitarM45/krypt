from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30))
    public_message_key: Mapped[str] = mapped_column()