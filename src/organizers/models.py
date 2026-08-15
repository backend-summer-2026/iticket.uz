from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.core.database import Base, UUIDMixin, TimestampMixin
from src.organizers.constants import OrganizerStatus
from src.users.models import User


class Organizer(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "organizers"

    company_name: Mapped[str] = mapped_column("company_name", nullable=False)
    description: Mapped[str] = mapped_column("description", nullable=False)
    status: Mapped[OrganizerStatus] = mapped_column(
        "status", nullable=False, default=OrganizerStatus.PENDING
    )
    description: Mapped[str | None] = mapped_column("description", nullable=True)
    status: Mapped[OrganizerStatus] = mapped_column("status", nullable=False, default=OrganizerStatus.PENDING)

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    approved_by: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=True)

    user: Mapped['User'] = relationship(foreign_keys=[user_id], back_populates='organizer')
    approver: Mapped['User | None'] = relationship(foreign_keys=[approved_by])
