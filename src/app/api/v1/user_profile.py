from fastapi import APIRouter
from fastapi import Response
from schema.profile import UserProfile
from model.document import Document


router = APIRouter()
user_document = Document()

@router.post("/create_user")
async def _create_user(body: UserProfile):
    user_request = body.dict()
    user_id = user_request["user_id"]
    user_info = {
        "age": user_request["age"],
        "sex": user_request["sex"],
        "extra_info": user_request["extra_info"]
    }
    status, message = user_document.insert_user(user_id, user_info)
    return {"sucess": status, "error": message}
