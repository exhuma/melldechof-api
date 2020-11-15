from typing import Optional
from uuid import UUID

import httpx
from fastapi import Depends, FastAPI, status, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from melldechof.db import Base, SessionLocal, engine
from melldechof.localtypes import Presence
from pydantic import BaseSettings
from sqlalchemy.orm import Session
import melldechof.db as db

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


class Settings(BaseSettings):
    ics_url: str = "https://www.officeholidays.com/ics-clean/luxembourg"

    class Config:
        env_file = ".env"


settings = Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ical")
async def ical():
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.ics_url)
        return {"ics": response.text}


@app.put("/presence/{user_id}/{event_id}/{presence}")
async def store_presence(
    user_id: UUID, event_id: str, presence: Presence, response: Response, session: Session = Depends(get_db),
):
    user = session.query(db.User).get(user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User in this presence-object does not exist")

    entity = session.query(db.Presence).get({
        "event_id": event_id,
        "user_id": user_id,
    })
    if not entity:
        entity = db.Presence(
            event_id=event_id,
            user=user,
            presence=presence,
        )
        session.add(entity)
        response.status_code = 201
    else:
        entity.presence = presence
        response.status_code = 200
    session.commit()
    return {
        "eventId": event_id,
        "presence": presence,
        "userId": user_id,
    }