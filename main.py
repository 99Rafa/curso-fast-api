from typing import Optional

from fastapi import Body, FastAPI, Form, Path, Query, status

from models.location_models import Location
from models.login_models import LoginResponse
from models.person_models import *

app = FastAPI()


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
)
def home():
    return {"Hello": "World"}


# Request and response body
@app.post(
    path="/person/new",
    response_model=Person,
    # response_model_exclude=["password"],
    status_code=status.HTTP_201_CREATED,
)
def create_person(person: CreatePersonRequest = Body(...)):
    return person


# Validations: Query parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
)
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=3,
        max_length=50,
        title="Person name",
        description="This is the person name, it's between 1 and 50 characters",
        example=1,
    ),
    age: int = Query(
        # This makes age obligatory which is not a recommended practice
        ...,
        title="Person age",
        description="This is the person age, it's required",
        example=18,
    ),
):
    return {name: age}


# Validations: Path parameters
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person id",
        description="This is the person id.",
        example=1,
    )
):
    return {person_id: "It exists"}


# Validations: Request body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK,
)
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID.",
        example=1,
    ),
    person: Person = Body(...),
    location: Location = Body(...),
):
    result = dict(person)
    result.update(dict(location))
    return result


@app.post(
    path="/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
def login(
    username: str = Form(...),
    password: str = Form(...),
):
    return LoginResponse(username=username)
