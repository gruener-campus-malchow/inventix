import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


class Login(BaseModel):
    username: str
    password: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = sqlite3.connect("../sql/inventix.db")
db.row_factory = sqlite3.Row
c = db.cursor()


@app.post("/login")
async def login(login: Login):
    if login.username == "testuser" and login.password == "password":
        return {"logged_in": True}
    else:
        return {"logged_in": False}


@app.get("/searchItems")
async def search_items(name: str = "", notes: str = ""):
    print(repr(name))
    c.execute(
        """SELECT * FROM gegenstand WHERE name LIKE ? AND notes LIKE ? AND visible = TRUE""",
        ("%" + name + "%", "%" + notes + "%",),
    )
    raw_items = c.fetchall()
    items = []
    for item in raw_items:
        items.append({"id": item["id"], "name": item["name"], "notes": item["notes"]})

    return items
