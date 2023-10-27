import unicodedata
from typing import List, Optional

from langchain.chat_models.openai import _convert_dict_to_message

from chains.qa_chain import SimpleChain, openai
from prompts.query_extractor import SYSTEM_TEMPLATE
from schema import Message


class QueryExtractorChain(SimpleChain):
    def __init__(self):
        super().__init__()

    def reset_conversation(self, **kwargs):
        conversation = [
            {
                "role": "system",
                "content": SYSTEM_TEMPLATE
            }
        ]
        return conversation

    def prepare_conversation(self, human_prompt, history: List[Message] = [], **kwargs):
        conversation = self.reset_conversation(**kwargs)
        user_question = {
            "role": "user",
            "content": human_prompt.format(**kwargs)
        }
        conversation.append(user_question)
        return conversation


class QueryExtractorLangchain(QueryExtractorChain):
    def __init__(self):
        super().__init__()

    def prepare_conversation(self, human_prompt, history: List[Message] = [], **kwargs):
        conversation, = super().prepare_conversation(human_prompt, history, **kwargs)
        return [[_convert_dict_to_message(mess) for mess in conversation]]

    def inference(self, conversation=[], streaming=False, callbacks=None):
        return self.llm.generate(conversation, callbacks=callbacks)

    def run(self, human_prompt, history: List[Message] = [], streaming=False, **kwargs):
        callbacks_streaming = kwargs.get("callbacks", None)

        conversation = self.prepare_conversation(human_prompt, history, **kwargs)

        response = self.inference(conversation, streaming, callbacks_streaming)
        ai_message = Message(role='assistant', content=response.generations[0][0].text).dict()

        return ai_message
