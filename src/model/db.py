import pymongo

BE_DB="hackathongenai"
MESSAGE_COLLECTION="Message"

def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton
class Model:
    def __init__(self, host="local", port=27017, mongo_username="admin", mongo_password="password"):

        client = pymongo.MongoClient(host=host,
                                    username=mongo_username,
                                    password=mongo_password,
                                    port = port)
        be_db = client[BE_DB]
        self.message_col = be_db[MESSAGE_COLLECTION]