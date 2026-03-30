from fastapi import FastAPI,status,Depends,HTTPException
import models
from database import engine,SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine) ## use all tables registered and make them in mysql

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/",status_code=status.HTTP_200_OK )
async def user(user:None,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return {"message": "Welcome to the protected route!"}
    return({"user": user})