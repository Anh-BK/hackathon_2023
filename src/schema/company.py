from pydantic import BaseModel


class CompanyInsertSchema(BaseModel):
  company_name :str