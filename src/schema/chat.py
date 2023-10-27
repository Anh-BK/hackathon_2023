from pydantic import BaseModel
from typing import Union, List, Optional

class BaseRequest(BaseModel):
    user_id: str
    human_message: str
    company_name: str
    task: Optional[str]

class BaseResponse(BaseModel):
    AI_message: str
