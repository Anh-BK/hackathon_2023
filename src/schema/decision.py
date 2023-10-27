from pydantic import BaseModel

class DecisionResponse(BaseModel):
    necessary: str
    description: str
