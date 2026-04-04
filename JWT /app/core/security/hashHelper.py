## We use bcrypt for hashing passwords
# two static method 
from bcrypt import hashpw, gensalt, checkpw

class HashHelper:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool: ##hashed from db
        
        if checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
        else:
            return False
        
    @staticmethod ## has the plain password 
    ##gensalt() -> adds random salt to pw before hashing , 
    def get_password_hash(plain_password: str) -> str:
        return hashpw(plain_password.encode('utf-8'), gensalt()).decode('utf-8')

