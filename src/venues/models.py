from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, UUIDMixin

class Venue(Base, UUIDMixin):
    __tablename__ = "venues"
    
    name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
