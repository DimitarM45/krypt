from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID


class User(DeclarativeBase):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, )
