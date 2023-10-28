from pydantic import BaseModel
from typing import Optional


class CompanyRequest(BaseModel):
  company_id :str
  is_useful: Optional[bool]

class ComparisionRequest(BaseModel):
  context_1: str
  context_2: str