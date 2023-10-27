from config.load_env import ENV
from .db import Model

env = ENV()
MONGODB_HOST = env.MONGODB_HOST
MONGODB_PORT = env.MONGODB_PORT
db = Model(MONGODB_HOST, MONGODB_PORT)

class Document:
    def get_info(self, user_id):
        user_data = db.message_col.find_one({"user_id": user_id})
        if user_data != None:
            user_info = user_data["user_info"]
            return user_info
        else:
            raise ValueError("User info doesn't exist!")
    
    def get_avatar(self, user_id):
        user_data = db.message_col.find_one({"user_id": user_id})
        image_bytes = user_data["avatar"]
        return image_bytes

    def insert_user(self, user_id, user_info):
        try:
            record = {
                "user_id": user_id,
                "user_info": user_info,
                "avatar": image_bytes,
                "conversation": []
            }
            db.message_col.insert_one(record)
            return True, ""
        except Exception as e:
            return False, e

    def get_history(self, user_id):
        user_data = db.message_col.find_one({"user_id": user_id})
        conversation = user_data["conversation"]
        return conversation

    def update_history(self, user_id, conversation):
        filter = {'user_id': user_id}
        print(f"history: {conversation}")
        new_conversation = { "$set": { 'conversation': conversation } }
        db.message_col.update_one(filter, new_conversation)
        return True

if __name__ == "__main__":
    document = Document()
    user_info = {
        "age": 24,
        "sex": "nam",
        "extra_info": None
    }
    chat_history = [
        {
            "role": "user",
            "content": ""
        },
        {
            "role": "assistant",
            "content": ""
        }
    ]
    #_ = document.insert_user("", user_info)
