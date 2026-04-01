## Sign up and Sign in 
#Authorize : grant access based on the user role
##Authentication : verify the identity of the user --> receive token 
from fastapi import APIRouter, Depends, HTTPException, status

auth_router = APIRouter()

@auth_router.post("/login")
def login():
    return {"message": "User logged in successfully"}

@auth_router.post("/signup")
def signup():
    return {"message": "User signed up successfully"}
