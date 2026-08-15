from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(example="123e4567-e89b-12d3-a456-426614174000") # type: ignore
    email: EmailStr = Field(example="user@example.com") # type: ignore
    is_active: Optional[bool] = Field(default=True, example=True) # type: ignore
    is_superuser: Optional[bool] = Field(default=False, example=False) # type: ignore
