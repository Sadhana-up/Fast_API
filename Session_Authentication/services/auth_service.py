## logic for signing or logging in 
#Match password and username 
from repositories.user_repo import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, username: str, password: str):
        user = self.user_repo.get_user(username)

        if not user:
            return None

        if user["password"] != password:
            return None

        return user