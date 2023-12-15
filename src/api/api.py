from fastapi import APIRouter

from src.api.endpoints import api_signup
from src.api.endpoints import api_signin
api_router = APIRouter()

api_router.include_router(api_signup.router, prefix='/signup')
api_router.include_router(api_signin.router, prefix='/signin')
