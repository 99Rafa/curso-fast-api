from typing import Optional

from fastapi import Body, FastAPI, Path, Query

from models import Person

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


# Request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    person
    return person


# Validations: Query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=3,
        max_length=50,
        title="Person name",
        description="This is the person name, it's between 1 and 50 characters",
    ),
    age: int = Query(
        # This makes age obligatory which is not a recommended practice
        ...,
        title="Person age",
        description="This is the person age, it's required",
    ),
):
    return {name: age}


# Validations: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person id",
        description="This is the person id.",
    )
):
    return {person_id: "It exists"}
