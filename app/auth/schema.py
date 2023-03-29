import uuid
from typing import Optional

from pydantic import BaseModel


class LoginRequest(BaseModel):
    secret_id: uuid.UUID
    secret_key: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: Optional[str] = None
