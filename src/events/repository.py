from sqlalchemy import select

from src.core.database import AsyncSession
from src.events.models import Event


class EventRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_event(self, event: Event) -> Event:
        self.db.add(event)
        await self.db.commit()
        await self.db.refresh(event)
        return event

    async def get_events(
        self,
    ) -> list[Event]:
        events = await self.db.execute(select(Event))
        return events.scalars()  # type: ignore
