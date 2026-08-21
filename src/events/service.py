from src.events.schemas import EventCreate
from src.events.repository import EventRepository
from src.organizers.models import Organizer
from src.events.models import Event


class EventService:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def create_event(self, data: EventCreate, organizer: Organizer) -> Event:
        return await self.repository.create_event(
            Event(
                organizer_id=organizer.id,
                venue_id=data.venue_id,
                category_id=data.category_id,
                title=data.title,
                slug=data.slug,
                description=data.description,
                poster_url=data.poster_url,
                start_datetime=data.start_datetime,
                end_datetime=data.end_datetime,
            )
        )

    async def get_events(self) -> list[Event]:
        return await self.repository.get_events()  # type: ignore
