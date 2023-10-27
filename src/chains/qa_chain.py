from typing import List
import openai
from llms import get_llm
from config.load_env import ENV
from langchain.chat_models.openai import _convert_dict_to_message
from constant.prompt import PROMPT_TYPES
from utils import convert_ai_message
from schema import Message

env = ENV()

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = env.AZ_OAI_VERSION
openai.api_base = env.AZ_OAI_BASE
openai.api_key = env.OPENAI_KEY

class SimpleChain:
    def __init__(self):
        self.chatbot_name = "",
        self.prompt = None,
        self.llm = get_llm(
            model_name=env.AZ_OAI_MODEL,
            temperature=0.8,
            max_new_tokens=2048
        )

    def reset_conversation(self, mode: str, **kwargs):
        conversation = [
            {
                "role": "system",
                "content": PROMPT_TYPES[mode]["system"].format(chatbot_name=self.chatbot_name, **kwargs)
            }
        ]
        return conversation

    def run(self, prompt_mode, history: List[Message], streaming=False, **kwargs) -> dict:
        conversation = self.reset_conversation(prompt_mode, PROMPT_TYPES, **kwargs)
        user_question = {
            "role": "user",
            "content": PROMPT_TYPES[prompt_mode]["user"].format(
                chatbot_name=self.chatbot_name,
                **kwargs
            )
        }
        
        _ = self.handle_history(history=history, conversation=conversation)
        conversation.append(user_question)
        conversation = [[_convert_dict_to_message(mess) for mess in conversation]]

        out = self.llm.generate(conversation)
        ai_message = convert_ai_message(out.generations[0][0].text)
        return ai_message

    def query(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def handle_history(self, history, conversation):
        for message in history:
            conversation.extend(
                [
                    {
                        'role': message["role"],
                        'content': message["content"]
                    }

                ]
            )

if __name__ == "__main__":
    simple_query = SimpleChain()
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
    message = simple_query.query(prompt_type=PROMPT_TYPES, history=chat_history,question="")
    print(message["content"])
