import uuid
import datetime
from typing import List

from pydantic import BaseModel


class Authorization(BaseModel):
    uuid: uuid.UUID
    partner_uuid: uuid.UUID
    status: str
    api_key: str
    api_secret: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class Partner(BaseModel):
    uuid: uuid.UUID
    first_name: str
    last_name: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    authorizations: List[Authorization] = []

    class Config:
        orm_mode = True
