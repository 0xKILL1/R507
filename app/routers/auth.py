from pydantic import BaseModel
import passlib
from typing import Optional
import jwt
from passlib.context import CryptContext

SECRET_KEY = "awwDzPmS7pohFjVcE4zwemuVBAyWnr1vUx2NSoCPHAuiTCMkRC0IQCt8FuFwe5LfOPteC4KSvynDwVfBdlih6g=="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440 #->1 jour

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Requete(BaseModel):
    mail:str
    mdp:str

class Token(BaseModel):
    token:str

def toHash(psswd:str)->str:
    return pwd_context.hash(psswd)

def verify_password(psswd_clair: str, psswd_hache_bdd: str) -> bool:
    return pwd_context.verify(psswd_clair, psswd_hache_bdd)

def create_access_token():
    pass

