from typing import List
import openai
from llms import get_llm
from config.load_env import ENV
from langchain.chat_models.openai import _convert_dict_to_message
from chains.qa_chain import SimpleChain
from constant.prompt import PROMPT_TYPES
from utils import convert_ai_message
from schema import Message

env = ENV()

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = env.AZ_OAI_VERSION
openai.api_base = env.AZ_OAI_BASE
openai.api_key = env.OPENAI_KEY

class ComparisionChain(SimpleChain):
    def __init__(self):
        super().__init__()

    def run(self, prompt_type, **kwargs) -> dict:
        conversation = self.reset_conversation("comparision", **kwargs)
        context_1, context_2 = kwargs.get("contexts")
        user_question = {
            "role": "user",
            "content": prompt_type["comparision"]["user"].format(context_1=context_1, context_2=context_2)
        }

        conversation.append(user_question)
        conversation = [[_convert_dict_to_message(mess) for mess in conversation]]

        out = self.llm.generate(conversation)
        ai_message = convert_ai_message(out.generations[0][0].text)
        return ai_message

    def query(self, *args, **kwargs):
        return self.run(*args, **kwargs)

if __name__ == "__main__":
    simple_query = ComparisionChain()
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