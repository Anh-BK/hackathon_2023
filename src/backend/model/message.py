from config.load_env import ENV
from .db import Model
from datetime import datetime
from bson.objectid import ObjectId

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
    
    def get_messages(self, company_id, is_useful):

        if is_useful != None:
            messages = db.message_col.find({
                "company_id": company_id,
                "is_useful": is_useful}
                )
        else:
            messages = db.message_col.find({"company_id": company_id})
        records = []
        for message in messages:
            message["_id"] = str(message["_id"])
            records.append(message)
        return records
  
    def update_status(self, message_id, is_useful):
        filter = {'_id': ObjectId(message_id)}
        new_conversation = { "$set": { 'is_useful':  is_useful} }
        db.message_col.update_one(filter, new_conversation)
        return True
    
    def insert_message(self, role, message, company_name, **kwargs):
        try:
            record = {
                "message": message,
                "role": role,
                "company_id":company_name,
                "is_useful": False,
                **kwargs
            }
            record['created_at'] = datetime.now()
            record['updated_at'] = record['created_at']
            db_result = db.message_col.insert_one(record)
            return True, db_result
        except Exception as e:
            return False, e

if __name__ == "__main__":
    message_dao = Message()
    # _ = message_dao.insert_message("user", message="hello world!", company_name="FPT")
    records = message_dao.get_messages("FPT")
    print(records)