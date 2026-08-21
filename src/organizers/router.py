from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, Body

from src.organizers.models import Organizer
from src.core.database import get_db, AsyncSession
from src.users.models import User
from src.auth.dependencies import get_current_active_user, get_current_active_superuser
from src.organizers.schemas import OrganizerCreate, OrganizerResponse, OrganizerApprove
from src.organizers.repository import OrganizerRepository
from src.organizers.service import OrganizerService

router = APIRouter()


@router.post("/", response_model=OrganizerResponse)
async def create_organizer(
    data: OrganizerCreate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
) -> Organizer:
    organizer_repository = OrganizerRepository(db)
    organizer_service = OrganizerService(organizer_repository)
    created_organizer = await organizer_service.create_organizer(data, current_user)
    return created_organizer


@router.get("/", response_model=OrganizerResponse)
async def get_organizer(
    current_user: User = Depends(get_current_active_user), db: AsyncSession = Depends(get_db)
) -> Organizer:
    organizer_repository = OrganizerRepository(db)
    organizer_service = OrganizerService(organizer_repository)
    organizer = await organizer_service.get_organizer_by_user(current_user)
    return organizer


@router.post("/approve", response_model=OrganizerResponse)
async def approve_organization(
    data: OrganizerApprove = Body(),
    current_user: User = Depends(get_current_active_superuser),
    db: AsyncSession = Depends(get_db),
) -> Organizer:
    organizer_repository = OrganizerRepository(db)
    organizer_service = OrganizerService(organizer_repository)
    organizer = await organizer_service.approve_oranization(current_user, data.id)
    return organizer


@router.post("/reject", response_model=OrganizerResponse)
async def reject_organization(
    data: OrganizerApprove = Body(),
    current_user: User = Depends(get_current_active_superuser),
    db: AsyncSession = Depends(get_db),
) -> Organizer:
    organizer_repository = OrganizerRepository(db)
    organizer_service = OrganizerService(organizer_repository)
    organizer = await organizer_service.reject_oranization(current_user, data.id)
    return organizer
