from fastapi import APIRouter

from chains.comparision_chain import ComparisionChain
from constant.prompt import PROMPT_TYPES
from schema.company import ComparisionRequest
from model.document import Document
from model.message import Message

router = APIRouter()
comparision_chain = ComparisionChain()
message_dao = Message()

@router.post("/comparing")
async def _comparing(body: ComparisionRequest):
    user_request = body.dict()
    first_context = user_request["context_1"]
    second_context = user_request["context_2"]
    contexts = [first_context, second_context]
    assitant_output = comparision_chain.query(contexts=contexts)
    return assitant_output
