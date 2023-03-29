from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.schema import LoginRequest

import app.database.database as db
from app.auth.jwt import create_access_token
from app.services.partner_service import get_partner_by_api_key

router = APIRouter(
    tags=["token"],
    prefix="/token"
)


@router.post("/new")
def create_token(request: LoginRequest, database: Session = Depends(db.get_db)):
    if partner := get_partner_by_api_key(request, database):
        # Generate JWT token
        return {"access_token": create_access_token(partner),
                "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )