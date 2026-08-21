from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class CategoryCreate(BaseModel):
    name: str = Field(min_length=5)
    slug: str = Field(min_length=5)


class CategoryResponse(BaseModel):
    id: UUID
    name: str = Field(min_length=5)
    slug: str = Field(min_length=5)

    model_config = ConfigDict(from_attributes=True)


class CategoryResponseList(BaseModel):
    categories: list[CategoryResponse]

    model_config = ConfigDict(from_attributes=True)
