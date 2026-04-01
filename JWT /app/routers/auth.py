## Sign up and Sign in 
#Authorize : grant access based on the user role
##Authentication : verify the identity of the user --> receive token 
from fastapi import APIRouter, Depends, HTTPException, status
from app.db.schema.user import UserInCreate, UserInLogin, UserWithToken


auth_router = APIRouter()

@auth_router.post("/login")
def login(loginDetails: UserInLogin):
    return {"message": "User logged in successfully"}

@auth_router.post("/signup")
def signup(signupDetails: UserInCreate):
    return {"message": "User signed up successfully"}
