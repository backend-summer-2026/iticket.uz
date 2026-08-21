from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class OrganizerApprove(BaseModel):
    id: UUID


class OrganizerCreate(BaseModel):
    company_name: str = Field(min_length=5)
    description: str = ""


class OrganizerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    company_name: str = Field(min_length=5)
    description: str | None = None
    status: str

    user_id: UUID
    approved_by: UUID | None = Field(example="123e4567-e89b-12d3-a456-426614174000")  # type: ignore
