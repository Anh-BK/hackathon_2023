from pydantic import BaseModel
from typing import Union, List, Optional
from message import Message

class BaseRequest(BaseModel):
    user_id: str
    human_message: str
    company_name: str
    history: List[Message]
    task: Optional[str]

class BaseResponse(BaseModel):
    AI_message: str
