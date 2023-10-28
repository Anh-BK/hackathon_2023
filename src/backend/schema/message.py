from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    content: str
    role: str

class UpdatingRequest(BaseModel):
    message_id: str
    is_useful: bool
