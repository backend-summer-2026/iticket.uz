from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, UUIDMixin

class Category(Base, UUIDMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)

    events: Mapped[List["Event"]] = relationship(back_populates="category")
