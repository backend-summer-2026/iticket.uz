from uuid import UUID

from sqlalchemy import select
from fastapi import HTTPException, status

from src.core.database import AsyncSession
from src.organizers.models import Organizer
from src.users.models import User
from src.organizers.constants import OrganizerStatus


class OrganizerRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_organizer_by_user(self, user: User) -> Organizer | None:
        stmt = select(Organizer).where(Organizer.user_id == user.id)
        result = await self.session.execute(stmt)
        organizer = result.scalar_one_or_none()
        return organizer

    async def create_organizer(self, organizer: Organizer) -> Organizer:
        self.session.add(organizer)
        await self.session.commit()
        await self.session.refresh(organizer)
        return organizer

    async def approve_organization(self, user: User, id: UUID) -> Organizer:
        organizer = await self.get_organizer_by_id(id)
        if not organizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer mavjud emas",
            )

        organizer.status = OrganizerStatus.APPROVED # type: ignore
        organizer.approved_by = user.id # type: ignore

        self.session.add(organizer)
        await self.session.commit()
        await self.session.refresh(organizer)
        return organizer

    async def reject_organization(self, user: User, id: UUID) -> Organizer:
        organizer = await self.get_organizer_by_id(id)
        if not organizer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organizer mavjud emas",
            )

        organizer.status = OrganizerStatus.REJECTED # type: ignore
        organizer.approved_by = user.id # type: ignore

        self.session.add(organizer)
        await self.session.commit()
        await self.session.refresh(organizer)
        return organizer

    async def get_organizer_by_id(self, id: UUID) -> Organizer | None:
        stmt = select(Organizer).where(Organizer.id == id)
        result = await self.session.execute(stmt)
        organizer = result.scalar_one_or_none()
        return organizer
