from fastapi import APIRouter, Request, Form
from services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()