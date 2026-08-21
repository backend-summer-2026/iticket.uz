from sqlalchemy import select

from src.core.database import AsyncSession
from src.venues.models import Venue


class VenueRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_venue_by_name(self, name: str) -> Venue | None:
        stmt = select(Venue).where(Venue.name == name)
        result = await self.db.execute(stmt)
        venue = result.scalar_one_or_none()
        return venue

    async def create_venue(self, venue: Venue) -> Venue:
        self.db.add(venue)
        await self.db.commit()
        await self.db.refresh(venue)
        return venue

    async def get_venues(self) -> list[Venue]:
        stmt = select(Venue)
        result = await self.db.execute(stmt)
        return result.scalars()  # type: ignore
