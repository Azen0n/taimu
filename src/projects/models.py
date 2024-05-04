from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import Base
from src.issues.models import Issue


class Project(Base):
    """Database model for projects."""

    __tablename__ = 'project'
    title: Mapped[str] = mapped_column(String(255))
    key: Mapped[str] = mapped_column(String(10))
    description: Mapped[str | None]

    issues: Mapped[list[Issue]] = relationship('Issue', back_populates='project')

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime | None]
    deleted_at: Mapped[datetime | None]
