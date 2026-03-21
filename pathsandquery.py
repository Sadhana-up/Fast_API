from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def main():
    return {"Message" : "Hello you're using fastapi."}

@app.get("/msg/{name}")

async def givename(name:str):
    return {"Message " : f"hello {name}"}

@app.get("/sum/")
async def sum(a:int,b:int):
    return {"sum is " : a+b}

@app.get("/prod/")
async def prod(x:int,y:int):
    return {"Products is ": x*y}
