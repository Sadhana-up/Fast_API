from pydantic import BaseModel,EmailStr
from typing import Union

class UserInCreate(BaseModel): ## user signs up
    email: EmailStr
    password: str
    username: str

class UserOutResponse(BaseModel):
    id: int
    email: EmailStr
    username: str


class UserInUpdate(BaseModel): 
    id: int
    email:Union[EmailStr, None] = None
    username: Union[str, None] = None
    password : Union[str, None] = None

class UserInLogin(BaseModel):
    email: EmailStr
    password: str

class UserWithToken(BaseModel): ## app -> users 
    token: str


  
