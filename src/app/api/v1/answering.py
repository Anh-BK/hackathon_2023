from fastapi import APIRouter

from chains.qa_chain import SimpleChain
from chains.searching_chain import OnlineSearch
from constant.prompt import PROMPT_TYPES
from schema.chat import BaseRequest
from model.document import Document
from model.message import Message

router = APIRouter()
searching_chat = OnlineSearch()
user_document = Document()
message_dao = Message()

@router.post("/answering")
async def _answering(body: BaseRequest):
    user_request = body.dict()
    question = user_request["human_message"]
    task = user_request["task"]
    history = user_request.get("history", None)
    company_name = user_request["company_name"]
    assitant_output, citations = searching_chat.query(question=question, history=history, task=task)
    _ = message_dao.insert_message("user", question, company_name)
    _ = message_dao.insert_message("assistant", assitant_output, company_name, citations=citations)
    return {
        "answer": assitant_output,
        "citation": citations
    }
