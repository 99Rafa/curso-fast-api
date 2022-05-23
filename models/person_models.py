from asyncio.base_subprocess import BaseSubprocessTransport
from typing import Optional

from pydantic import BaseModel, Field

from enums import HairColor


class Person(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=0)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Rafael",
                "last_name": "Aguirre",
                "age": 22,
                "hair_color": "black",
                "is_married": False,
            }
        }


class CreatePersonRequest(Person):
    password: str = Field(..., min_length=8)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Rafael",
                "last_name": "Aguirre",
                "age": 22,
                "hair_color": "black",
                "is_married": False,
                "password": "12345678",
            }
        }
