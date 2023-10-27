from typing import List, Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    user_id: str
    age: int
    sex: str
    extra_info: Optional[str]=None
