# Login Simulation
# Model: Login
# username: str
# password: str
# Endpoint: /login/
# Return:

from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    username : str
    password : str

app = FastAPI()

@app.post("/login/")

async def get_msg(user : User):
    return{"message": f"login sucessful for {User.username}" }
