from typing import Optional

import httpx
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ical")
async def ical():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://calendar.google.com/calendar/ical/cug6ctnnqdg31q6d82vba8gjkc%40group.calendar.google.com/public/basic.ics")
        return {"ics": response.text}


@app.get("/fail")
def fail():
    return JSONResponse(status_code=500, content="Error")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
