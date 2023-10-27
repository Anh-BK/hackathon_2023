from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    content: str
    role: str
