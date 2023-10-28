from fastapi import APIRouter

from schema.chat import BaseRequest
from model.company import Company
from fastapi.responses import JSONResponse
from schema.company import CompanyInsertSchema

router = APIRouter()
company_document = Company()

@router.post("")
async def add_company(body:CompanyInsertSchema):
    user_request = body.dict()
    company_name = user_request["company_name"]
    await company_document.insert_company(company_name=company_name)
    return JSONResponse({"message":"add success"})

@router.get("")
async def add_company():
    _,result = await company_document.get_company()
    print(result)
    return JSONResponse(content="")

