from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import Base

if TYPE_CHECKING:
    from src.projects.models import Project


class Issue(Base):
    """Database model for issues."""

    __tablename__ = 'issue'
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None]

    parent_id: Mapped[int] = mapped_column(ForeignKey('issue.id'), nullable=True)
    parent: Mapped[Issue] = relationship(back_populates='child_issues')
    child_issues: Mapped[list[Issue]] = relationship('Issue')

    project_id: Mapped[int] = mapped_column(ForeignKey('project.id'))
    project: Mapped[Project] = relationship(back_populates='issues')
    type_id: Mapped[int] = mapped_column(ForeignKey('issue_type.id'))
    type: Mapped[IssueType] = relationship('IssueType')
    status_id: Mapped[int] = mapped_column(ForeignKey('issue_status.id'))
    status: Mapped[IssueStatus] = relationship('IssueStatus')

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime | None]
    deleted_at: Mapped[datetime | None]


class IssueType(Base):
    """Database model for issue types."""

    __tablename__ = 'issue_type'
    name: Mapped[str] = mapped_column(String(64))


class IssueStatus(Base):
    """Database model for issue statuses."""

    __tablename__ = 'issue_status'
    name: Mapped[str] = mapped_column(String(64))
