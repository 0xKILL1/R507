from typing import Annotated
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt
from sqlmodel import Session, select
from passlib.context import CryptContext
from ..bdd import engine
from ..models import User

SECRET_KEY = "awwDzPmS7pohFjVcE4zwemuVBAyWnr1vUx2NSoCPHAuiTCMkRC0IQCt8FuFwe5LfOPteC4KSvynDwVfBdlih6g=="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/supervision/token")

def init_root_user():
    from ..models import User
    with Session(engine) as session:
        root = session.exec(select(User).where(User.email == "root@gmail.com")).first()
        if root:
            return

        hashed = pwd_context.hash("bonjour")
        new_user = User(
            email="root@gmail.com",
            MdpHash=hashed
        )
        session.add(new_user)
        session.commit()



init_root_user()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_db(session: Session, email: str):
    user_db = session.exec(select(User).where(User.email == email)).first()
    if not user_db:
        return None
    return {
        "email": user_db.email,
        "hashed_password": user_db.MdpHash
    }

def authenticate_user(session: Session, email: str, password: str):
    user = get_user_db(session, email)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token invalide ou expiré",
            )
        return email
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide",
        )
