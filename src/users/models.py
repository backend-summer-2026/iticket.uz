from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base, UUIDMixin, TimestampMixin

if TYPE_CHECKING:
    from src.organizers.models import Organizer


class User(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)

    organizer: Mapped['Organizer'] = relationship(
        back_populates='user', foreign_keys='Organizer.user_id'
    )
