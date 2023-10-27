from config.load_env import ENV
from constant.contants import ASSISTANT
from schema import Message

env = ENV()


def convert_ai_message(message: str):
    ai_message = Message(role=ASSISTANT, content=message).dict()
    return ai_message

def split_bullet_point(bullet_point: str):
    split_value = bullet_point.split("- ")
    if len(split_value) > 1:
        return split_value[1]
    return split_value[0]
