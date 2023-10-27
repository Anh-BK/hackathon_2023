from sys import prefix
from fastapi import APIRouter
from .answering import router as answering_router
from .decision import router as decision_router
from .user_profile import router as profile_router

api_v1_router = APIRouter()
api_v1_router.include_router(answering_router, prefix="/answering",tags=["Answering"])
api_v1_router.include_router(decision_router, prefix="/decision", tags=["Decision"])
api_v1_router.include_router(profile_router, prefix="/profile",tags=["Profile"])
