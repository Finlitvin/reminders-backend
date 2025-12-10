from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ReminderModel(Base):
    __tablename__ = "reminder"

    id: Mapped[int] = mapped_column(primary_key=True)

    tittle: Mapped[int]
    description: Mapped[str]

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
