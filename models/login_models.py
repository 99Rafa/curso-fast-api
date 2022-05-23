from pydantic import BaseModel, Field


class LoginResponse(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="Rafa2022",
    )
    message: str = Field(
        default="Login successful",
    )
