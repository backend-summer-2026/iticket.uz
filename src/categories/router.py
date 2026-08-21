from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, Body

from src.core.database import get_db, AsyncSession
from src.users.models import User
from src.auth.dependencies import get_current_active_user, get_current_active_superuser

from src.categories.models import Category
from src.categories.schemas import CategoryCreate, CategoryResponse, CategoryResponseList
from src.categories.repository import CategoryRepository
from src.categories.service import CategoryService


router = APIRouter()


@router.post("/", response_model=CategoryResponse)
async def create_category(
    data: CategoryCreate,
    user: User = Depends(get_current_active_superuser),
    db: AsyncSession = Depends(get_db),
) -> Category:
    category_repository = CategoryRepository(db)
    category_service = CategoryService(category_repository)
    new_category = await category_service.create_category(data)
    return new_category


@router.get("/", response_model=CategoryResponseList)
async def get_category_list(
    user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    category_repository = CategoryRepository(db)
    category_service = CategoryService(category_repository)
    categories: list[Category] = await category_service.get_all_categories()
    return CategoryResponseList(categories=categories)  # type: ignore
