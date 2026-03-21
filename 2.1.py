from pydantic import BaseModel
from fastapi import FastAPI

# Create a POST endpoint /student/ with:
# name: str
# roll_no: int
# course: str

app = FastAPI()

class User(BaseModel):# fastapi le chei request ma pathako json afri padhxa 
    # validate garxa using yo pydantic model 
    # ani tespaxi ok vayesi chei balla ppst method run hunxa 
    name : str 
    roll_no : int
    course : str 

@app.post("/student/")

async def create_student(user : User):
    
    return {"message" : "student created",
    "Student" : user}



