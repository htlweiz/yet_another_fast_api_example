from typing import Union

from fastapi import FastAPI
import pydantic


class Person(pydantic.BaseModel):
    id: int
    name: str
    first_name: str


app = FastAPI()

robert = Person(id=0, first_name="Robert", name="Ulmer")

persons = [robert]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/persons/")
def read_persons():
    return persons


@app.post("/persons/")
async def create_item(person: Person):
    persons.append(person)
    return person
