from fastapi import FastAPI

app = FastAPI()
# Use get when u  want to retrieve data from api


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")

async def greet_name(name:str):
    return {f"Namaste {name} "}

@app.get("/msg/{message}")

async def get_message(message:str):
    return {" message": f"{message} "}

@app.get("/add/")

async def sum(a:int,b : int):
    return {"Sum is " : a+b}
