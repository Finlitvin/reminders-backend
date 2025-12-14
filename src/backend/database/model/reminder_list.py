from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ReminderListModel(Base):
    __tablename__ = "reminder_list"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    section = relationship(
        "SectionModel", back_populates="reminder_list", lazy="selectin"
    )
