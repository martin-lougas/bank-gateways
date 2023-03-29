from datetime import timezone
from fastapi import Depends, HTTPException,  status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from datetime import datetime, timedelta

from app.auth import schema
from app.database.models import AuthorizationModel

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(partner: AuthorizationModel):
    current_time = datetime.now(timezone.utc)
    to_encode = {
        "sub": str(partner.partner_uuid),
        "iat": current_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "iss": "https://dev-1q7x2x7e.us.auth0.com/",
        "aud": "https://dev-1q7x2x7e.us.auth0.com/api/v2/",
        "exp": (
            current_time
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        ),
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        uuid: str = payload.get("sub")
        if uuid is None:
            raise credentials_exception
        return schema.TokenData(uuid=uuid)
    except JWTError as e:
        raise credentials_exception from e


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(data, credentials_exception)
