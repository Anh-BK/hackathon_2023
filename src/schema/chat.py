from pydantic import BaseModel
from typing import Union, List, Optional, Literal
from .message import Message

class BaseRequest(BaseModel):
    human_message: str
    company_name: str
    history: Optional[List[Message]]
    task: Literal['extraction', 'interpretation', 'summarization']

class BaseResponse(BaseModel):
    AI_message: str
