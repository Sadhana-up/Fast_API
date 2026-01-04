# While get is visible in the server, it is unsafe 
# So we use post method when we have to send data to the server 
# Data only goes in the request body : used for user resgitration. create records
# example of request body {
#   "name": "Sadhana",
#   "age": 22
# }

from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    name : str 
    age : int 

app = FastAPI()

@app.post("/user")
async def create_user(user: User):
    return {
        "Message" :"helllo",
        "User": user
    }

