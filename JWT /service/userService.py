from app.db.repository.userRepo import UserRepository
from app.db.schema.user import UserInCreate, UserInLogin, UserInUpdate, UserOutResponse, UserWithToken
from app.core.security.hashHelper import HashHelper
from app.core.security.authHandler import AuthHandler
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

## make queries to db and return data to app

class UserService:

    def __init__(self,session: Session):
        # self.session = session
        self.__userRepo = UserRepository(session)
    
    def signup(self, user_details: UserInCreate) -> UserOutResponse:
        db_user = self.__userRepo.get_user_by_email(user_details.email)
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        hashed_password = HashHelper.get_password_hash(user_details.password)
        user_details.password = hashed_password
        new_user = self.__userRepo.create_user(user_details)
        return new_user
        
