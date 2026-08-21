from datetime import datetime
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.core.database import Base, UUIDMixin, TimestampMixin
from src.organizers.models import Organizer
from src.venues.models import Venue
from src.categories.models import Category


class EventStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CANCELLED = "cancelled"


class Event(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "events"

    organizer_id: Mapped[str] = mapped_column("organizer_id", ForeignKey("organizers.id"))
    venue_id: Mapped[str] = mapped_column("venue_id", ForeignKey("venues.id"))
    category_id: Mapped[str] = mapped_column("category_id", ForeignKey("categories.id"))
    title: Mapped[str] = mapped_column("title", nullable=False)
    slug: Mapped[str] = mapped_column("slug", nullable=False)
    description: Mapped[str] = mapped_column("description", nullable=True, default="")
    poster_url: Mapped[str] = mapped_column("poster_url", nullable=True, default="")
    start_datetime: Mapped[datetime] = mapped_column("start_datetime", nullable=False)
    end_datetime: Mapped[datetime] = mapped_column("end_datetime", nullable=False)
    status: Mapped[EventStatus] = mapped_column("status", nullable=False, default=EventStatus.DRAFT)
    banner_url: Mapped[str] = mapped_column("banner_url", nullable=True)

    organizer: Mapped[Organizer] = relationship(
        foreign_keys=[organizer_id], back_populates="events"
    )
    venue: Mapped[Venue] = relationship(foreign_keys=[venue_id], back_populates="events")
    category: Mapped[Category] = relationship(foreign_keys=[category_id], back_populates="events")
