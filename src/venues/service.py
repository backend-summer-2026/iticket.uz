from fastapi import HTTPException, status

from src.venues.repository import VenueRepository
from src.venues.schemas import VenueCreate
from src.venues.models import Venue


class VenueService:
    def __init__(self, repository: VenueRepository) -> None:
        self.repository = repository

    async def create_venue(self, data: VenueCreate) -> Venue:
        existing_venue = await self.repository.get_venue_by_name(data.name)
        if existing_venue:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Bunday venue oldin yaratilgan."
            )

        new_venue = await self.repository.create_venue(
            Venue(name=data.name, address=data.address, city=data.city, capacity=data.capacity)
        )

        return new_venue

    async def get_all_venus(self) -> list[Venue]:
        result = await self.repository.get_venues()
        return result
