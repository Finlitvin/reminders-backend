from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import JSON, ARRAY, Double, DateTime, Uuid
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
    # type_annotation_map = {
    #     dict[str, Any]: JSON,
    #     list[float]: ARRAY(Double),
    #     datetime: DateTime(timezone=True),
    #     UUID: Uuid,
    # }
