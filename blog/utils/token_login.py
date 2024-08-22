from datetime import datetime, timedelta
from jose import JWTError, jwt, ExpiredSignatureError
from ..schemas import schemas
from fastapi import  HTTPException,status
import secrets
import pytz
import os


# secret_key = secrets.token_bytes(32)
# print("secret_key", secret_key.hex())
zones = pytz.all_timezones
SECRET_KEY = os.environ.get("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
ALGORITHM = os.environ.get("ALGORITHM")


def create_access_token(data: dict):
    Pacific = pytz.timezone('US/Pacific') #America/Los_Angeles
    to_encode = data.copy()
    expire = datetime.now(Pacific) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload:
            email: str = payload.get("sub")
            return email
    except ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail=f"Token expired: {e}")
    except Exception as e:
        raise HTTPException(status_code=401, detail="An error occurred while verifying token")


    