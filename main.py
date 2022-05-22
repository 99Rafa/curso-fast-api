from typing import Optional

from fastapi import Body, FastAPI, Query

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
    name: Optional[str] = Query(default=None, min_length=3, max_length=50),
    # This makes age obligatory which is not a recommended practice
    age: int = Query(...),
):
    return {name: age}
