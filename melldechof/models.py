from typing import List
from uuid import UUID

from melldechof.localtypes import Presence as PresenceEnum
from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    email: str
    name: str

    class Config:
        orm_mode = True


class Presence(BaseModel):
    user_id: UUID
    event_id: str
    presence: PresenceEnum
    user_name: str

    class Config:
        orm_mode = True


class PresenceList(BaseModel):
    presences: List[Presence]