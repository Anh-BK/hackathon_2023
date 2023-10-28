from fastapi import APIRouter

from chains.qa_chain import SimpleChain
from chains.searching_chain import OnlineSearch
from constant.prompt import PROMPT_TYPES
from schema.company import CompanyRequest
from schema.message import UpdatingRequest
from model.document import Document
from model.message import Message

router = APIRouter()
searching_chat = OnlineSearch()
user_document = Document()
message_dao = Message()

@router.post("/get_messages")
async def _get_messages(body: CompanyRequest):
    user_request = body.dict()
    company_id = user_request["company_id"]
    is_useful = user_request["is_useful"]
    messages = message_dao.get_messages(company_id, is_useful)
    return messages

@router.post("/update_status")
async def _update_status(body: UpdatingRequest):
    user_request = body.dict()
    message_id = user_request["message_id"]
    is_useful = user_request["is_useful"]
    messages = message_dao.update_status(message_id, is_useful)
    return messages