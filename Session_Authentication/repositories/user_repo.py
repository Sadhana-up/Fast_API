##We are cresting a repostitory 
#because our router should not directly touch the database 
# so Flow is ROUTER->SERVICES->REPOSITORY->DATABASE


from database.fake_db import users

class UserRepository:
    def get_user(self, username: str):
        return users.get(username)