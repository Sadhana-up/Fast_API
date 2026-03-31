from datetime import datetime, timedelta
import os
from pathlib import Path
from typing import Optional, Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel
from models import User
from fastapi import APIRouter

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

SECRET_KEY = os.getenv("SECRET_KEY", "change_me_in_env")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") ## hashing and unhasing password
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login") ## token url for login

class CreateUserRequest(BaseModel): ## validare before puttin gin the db 
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/register", response_model=Token)
def register(user: CreateUserRequest, db: db_dependency):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = bcrypt_context.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

  