from asyncio.base_subprocess import BaseSubprocessTransport
from doctest import Example
from typing import Optional

from pydantic import BaseModel, Field

from enums import HairColor


class BasePerson(BaseModel):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Rafael",
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Aguirre",
    )
    age: int = Field(
        ...,
        gt=0,
        example=22,
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black",
    )
    is_married: Optional[bool] = Field(
        default=None,
        example=False,
    )


class Person(BasePerson):
    pass


class CreatePersonRequest(BasePerson):
    password: str = Field(
        ...,
        min_length=8,
        example="12345678",
    )
