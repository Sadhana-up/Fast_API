from .base import BaseRepository
from app.db.models import User
from app.db.schema.user import UserInCreate, UserInUpdate
##schema has models used bu the router 
## model has the acutal user table 
# so i want it to communicate with the user table and the user schema to create a user in the database and return the user details to the router so that it can be sent back to the client

class UserRepository(BaseRepository): ## inehrit from base repo 

    def create_user(self, user_data : UserInCreate) -> User:
        new_user = User(user_data.model_dump(exclude_none  = True)) ## dump info of users info to db 
  
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user) ## to get the new user details after commit 
        return new_user
    
    def user_exist_by_email(self, email: str) -> bool:

        return self.session.query(User).filter(User.email == email).first() is not None
    
    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()
    