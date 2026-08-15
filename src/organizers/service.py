from uuid import UUID

from fastapi import HTTPException, status

from src.organizers.models import Organizer
from src.organizers.repository import OrganizerRepository
from src.organizers.schemas import OrganizerCreate
from src.users.models import User


class OrganizerService:
    def __init__(self, organizer_repository: OrganizerRepository) -> None:
        self.organizer_repository = organizer_repository

    async def create_organizer(self, data: OrganizerCreate, user: User) -> Organizer:
        existing_oraganizer = await self.organizer_repository.get_organizer_by_user(user)
        if existing_oraganizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer allaqachon bor",
            )
        new_organizer = Organizer(company_name=data.company_name, description=data.description, user_id=str(user.id))
        return await self.organizer_repository.create_organizer(new_organizer)

    async def get_organizer_by_user(self, user: User) -> Organizer:
        existing_oraganizer = await self.organizer_repository.get_organizer_by_user(user)
        if not existing_oraganizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer allaqachon bor",
            )
        return existing_oraganizer

    async def approve_oranization(self, user: User, id: UUID) -> Organizer:
        existing_oraganizer = await self.organizer_repository.get_organizer_by_id(id)
        if not existing_oraganizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer allaqachon bor",
            )

        org = await self.organizer_repository.approve_organization(user, id)
        return org

    async def reject_oranization(self, user: User, id: UUID) -> Organizer:
        existing_oraganizer = await self.organizer_repository.get_organizer_by_id(id)
        if not existing_oraganizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer allaqachon bor",
            )

        org = await self.organizer_repository.reject_organization(user, id)
        return org
