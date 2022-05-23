from pydantic import BaseModel, Field


class Location(BaseModel):
    city: str = Field(..., example="Mexico city")
    state: str = Field(..., example="Mexico")
    country: str = Field(..., example="Mexico")
