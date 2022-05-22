from fastapi import Body, FastAPI

from models import Person

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


# Request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
