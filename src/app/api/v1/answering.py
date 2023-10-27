from fastapi import APIRouter

from chains.qa_chain import SimpleChain
from chains.searching_chain import OnlineSearch
from constant.prompt import PROMPT_TYPES
from schema.chat import BaseRequest
from model.document import Document

router = APIRouter()
searching_chat = OnlineSearch()
user_document = Document()

@router.post("/answering")
async def _answering(body: BaseRequest):
    user_request = body.dict()
    question = user_request["human_message"]
    user_id = user_request["user_id"]
    task = user_request["task"]
    company_name = user_request["company_name"]
    history = user_document.get_history(user_id)
    current_conversation = [
        {
            "role": "user",
            "content": question
        }
    ]
    assitant_output = searching_chat.query(question=question, history=history, task=task)
    current_conversation.append(assitant_output)
    history = history + current_conversation
    _ = user_document.update_history(user_id, history[-9:]) #last 3 converstions
    return assitant_output
