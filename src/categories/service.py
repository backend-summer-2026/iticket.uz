from fastapi import HTTPException, status

from src.categories.repository import CategoryRepository
from src.categories.schemas import CategoryCreate
from src.categories.models import Category


class CategoryService:
    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    async def create_category(self, data: CategoryCreate) -> Category:
        existing_category = await self.repository.get_category_by_name(data.name)
        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Bunday category oldin yaratilgan."
            )

        new_category = await self.repository.create_category(
            Category(name=data.name, slug=data.slug)
        )

        return new_category

    async def get_all_categories(self) -> list[Category]:
        result = await self.repository.get_categories()
        return result
