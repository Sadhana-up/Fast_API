from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("created")
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router=auth_router,tags=["auth"], prefix="/auth")


@app.get("/health")
def health_check():

    return {"status": "ok done !!!"}

