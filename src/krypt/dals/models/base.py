from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    was_created: Mapped[Optional[datetime]] = mapped_column(DateTime)
    was_deleted: Mapped[Optional[datetime]] = mapped_column(DateTime)
