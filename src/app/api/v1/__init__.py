from sys import prefix
from fastapi import APIRouter
from .answering import router as answering_router
from .conversation import router as conversation_router
from .comparision import router as comparision_router

api_v1_router = APIRouter()
api_v1_router.include_router(answering_router, prefix="/answering",tags=["Answering"])
api_v1_router.include_router(conversation_router, prefix="/conversation",tags=["Conversasion"])
api_v1_router.include_router(comparision_router, prefix="/comparision",tags=["Comparision"])

