from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from routers.auth import router
from config import SECRET_KEY

app = FastAPI()

app.add_middleware( ## request comes here first and then goes to router
    SessionMiddleware,
    secret_key=SECRET_KEY
)

app.include_router(router)

