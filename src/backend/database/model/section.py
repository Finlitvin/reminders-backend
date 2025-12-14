from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class SectionModel(Base):
    __tablename__ = "section"

    id: Mapped[int] = mapped_column(primary_key=True)
    reminder_list_id: Mapped[int] = mapped_column(
        ForeignKey("reminder_list.id", ondelete="CASCADE"), unique=True
    )

    name: Mapped[str]

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    reminder_list = relationship(
        "ReminderListModel", back_populates="section", lazy="selectin"
    )
    reminder = relationship(
        "ReminderModel", back_populates="section", lazy="selectin"
    )
