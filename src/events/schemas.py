from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class EventCreate(BaseModel):
    venue_id: UUID
    category_id: UUID
    title: str = Field(min_length=3)
    slug: str = ""
    description: str | None = None
    poster_url: str | None = None
    start_datetime: datetime
    end_datetime: datetime


class EventResponse(BaseModel):
    id: UUID
    organizer_id: UUID
    venue_id: UUID
    category_id: UUID
    title: str
    slug: str
    description: str | None = None
    poster_url: str | None = None
    start_datetime: datetime
    end_datetime: datetime
    status: str
    banner_url: str | None

    model_config = ConfigDict(from_attributes=True)


class EventListResponse(BaseModel):
    events: list[EventResponse]

    model_config = ConfigDict(from_attributes=True)
