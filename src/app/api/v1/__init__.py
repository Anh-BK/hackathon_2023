from sys import prefix
from fastapi import APIRouter
# from .answering import router as answering_router
from .company import router as company_router

api_v1_router = APIRouter()
# api_v1_router.include_router(answering_router, prefix="/answering",tags=["Answering"])
api_v1_router.include_router(company_router, prefix="/company",tags=["Company"])