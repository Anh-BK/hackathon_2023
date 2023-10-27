from pydantic import BaseModel
from typing import Union, List, Optional

class BaseRequest(BaseModel):
    user_id: str
    human_message: str
    is_used_predefined: Optional[bool]
    task: Optional[str]

class BaseResponse(BaseModel):
    AI_message: str
