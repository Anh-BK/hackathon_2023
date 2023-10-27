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
    history = user_document.get_history(user_id)
    current_conversation = [
        {
            "role": "user",
            "content": question
        }
    ]

    prompt_mode = "basic"
    if user_request["is_used_predefine"]:
        prompt_mode = "predefined_prompt"
    assitant_output = searching_chat.query(prompt_mode, question=question, history=history)
    current_conversation.append(assitant_output)
    history = history + current_conversation
    _ = user_document.update_history(user_id, history[-9:]) #last 3 converstions
    return assitant_output
