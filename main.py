from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
import models
from db import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine) #creates db 

class UserCreate(BaseModel):
    email: str
    password: str   

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_hashed_password = user.password + "notreallyhashed"
    new_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user