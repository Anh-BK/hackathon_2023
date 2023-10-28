from config.load_env import ENV
from .db import Model

env = ENV()
MONGODB_HOST = env.MONGODB_HOST
MONGODB_PORT = env.MONGODB_PORT
db = Model(MONGODB_HOST, MONGODB_PORT)

class Company:
  async def insert_company(self, company_name):
    try:
        record = {
            "company_name": company_name,
        }
        await db.company_col.insert_one(record)
        return True, ""
    except Exception as e:
        return False, e
    
  async def get_company(self):
    try:
        all_documents = await db.company_col.find().to_list()
        return True, all_documents
    except Exception as e:
        return False, e