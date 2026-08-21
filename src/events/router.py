from fastapi import APIRouter, Depends

from src.core.database import get_db, AsyncSession
from src.auth.dependencies import get_current_orginizer, get_current_active_user
from src.organizers.models import Organizer

from src.events.models import Event
from src.events.schemas import EventCreate, EventResponse, EventListResponse
from src.events.repository import EventRepository
from src.events.service import EventService


router = APIRouter()


@router.post("/", response_model=EventResponse)
async def create_event(
    data: EventCreate,
    organizer: Organizer = Depends(get_current_orginizer),
    db: AsyncSession = Depends(get_db),
) -> Event:
    repository = EventRepository(db)
    service = EventService(repository)
    event = await service.create_event(data, organizer)
    return event


@router.get("/", response_model=EventListResponse)
async def get_events(
    user: Organizer = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
) -> EventListResponse:
    repository = EventRepository(db)
    service = EventService(repository)
    events = await service.get_events()
    return EventListResponse(events=events)  # type: ignore
