from datetime import datetime, timedelta
from jose import JWTError, jwt, ExpiredSignatureError
from ..schemas import schemas
from fastapi import  HTTPException,status
import secrets
import pytz

# secret_key = secrets.token_bytes(32)
# print("secret_key", secret_key.hex())
zones = pytz.all_timezones

# print(zones) 
SECRET_KEY = "0784b83a2c066a29bfc49bbf17d292cf589a4a7c47519be52933c7754e9f936d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    # print(zones) 
    Pacific = pytz.timezone('US/Pacific') #America/Los_Angeles
    current=datetime.now(Pacific)
    # print(current)
    to_encode = data.copy()
    expire = datetime.now(Pacific) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    print("expire", expire)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print("token",type(encoded_jwt))
    return encoded_jwt

async def verify_token(token:str):
    print("here")
    try:
        print("token",type(token))
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("check payload",payload)
        if payload:
            email: str = payload.get("sub")
            print("check email",payload)
            return email
        if email is None:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
        token_data = schemas.TokenData(email=email)
    except ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail=f"Token expired: {e}")
    except Exception as e:
        raise HTTPException(status_code=401, detail="An error occurred while verifying token")


    