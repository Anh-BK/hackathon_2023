from config.load_env import ENV
from .db import Model
from datetime import datetime

env = ENV()
MONGODB_HOST = env.MONGODB_HOST
MONGODB_PORT = env.MONGODB_PORT
db = Model(MONGODB_HOST, MONGODB_PORT)

class Message:
    def insert_company(self, message, company_id, role):
        try:
            record = {
                "message": message,
                "role": role,
                "company_id":company_id,
                "useful": False,
            }
            record['created_at'] = datetime.now()
            record['updated_at'] = record['created_at']
            db.message_col.insert_one(record)
            return True, ""
        except Exception as e:
            return False, e
    
    def get_message_by_company_id(company_id):
        try:
            all_documents = db.company_col.find({"company_id": company_id})
            return True, all_documents
        except Exception as e:
            return False, e
    
    def get_history(self, user_id):
        user_data = db.message_col.find_one({"user_id": user_id})
        conversation = user_data["conversation"]
        return conversation
  
    def update_message(self, id, is_useful):
        filter = {'_id': id}
        new_conversation = { "$set": { 'is_useful':  is_useful} }
        db.message_col.update_one(filter, new_conversation)
        return True
    
    def insert_message(self, role, message, company_name):
        try:
            record = {
                "message": message,
                "role": role,
                "company_id":company_name,
                "is_useful": False,
            }
            record['created_at'] = datetime.now()
            record['updated_at'] = record['created_at']
            db.message_col.insert_one(record)
            return True, ""
        except Exception as e:
            return False, e