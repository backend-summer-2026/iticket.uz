from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class VenueCreate(BaseModel):
    name: str = Field(min_length=5)
    address: str = Field(min_length=3)
    city: str = Field(min_length=5)
    capacity: int = Field(gt=0)  # gt: >, ge: >=, lt: <, le: <=


class VenueResponse(BaseModel):
    id: UUID
    name: str = Field(min_length=5)
    address: str = Field(min_length=3)
    city: str = Field(min_length=5)
    capacity: int = Field(gt=0)  # gt: >, ge: >=, lt: <, le: <=

    model_config = ConfigDict(from_attributes=True)


class VenueResponseList(BaseModel):
    venues: list[VenueResponse]

    model_config = ConfigDict(from_attributes=True)
