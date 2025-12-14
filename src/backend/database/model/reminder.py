from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ReminderModel(Base):
    __tablename__ = "reminder"

    id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(
        ForeignKey("section.id", ondelete="CASCADE"), unique=True
    )

    tittle: Mapped[str]
    description: Mapped[str | None]

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    section = relationship(
        "SectionModel", back_populates="reminder", lazy="selectin"
    )
