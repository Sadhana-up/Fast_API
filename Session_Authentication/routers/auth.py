from fastapi import APIRouter, Request, Form
from services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = auth_service.login(username, password)

    if not user:
        return {"message": "Invalid credentials"}

    request.session["user"] = user["username"] ## CREATING SESSION 

    return {"message": "Logged in"}

@router.get("/profile")
def profile(request: Request):
    user = request.session.get("user")

    if not user:
        return {"message": "Not logged in"}

    return {"user": user}

@router.post("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out"}