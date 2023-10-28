from typing import Type, Any
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate)
from langchain.schema import LLMResult
from langchain.tools import BaseTool
from langchain.tools.google_search.tool import GoogleSearchResults
from langchain.utilities import GoogleSearchAPIWrapper

from config.load_env import ENV
from constant import ASSISTANT
from llms import get_llm
from llms.azure_openai import CustomAzureOpenAI
from prompts.internet_based_qa import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
from schema.message import Message
from schema.chat import BaseRequest

env = ENV()
ANSWERING_DEPLOYMENT = env.ANSWERING_MODEL

class CustomGoogleSearchTool(GoogleSearchResults):
    # name : str = 'Google Search Tool',
    # description= "Use this tool when user asks question that needs to look up contexts from the Internet ",

    def _run(self, query: str) -> str:
        results = self.api_wrapper.results(query, self.num_results)
        results = list(filter(lambda x: True if x.get("snippet") is not None else False, results))
        source_template = ('Content: {content}\nSource: [{title}]({link})')
        return "\n\n".join([source_template.format(content=res["snippet"],
                                                   title=res["title"],
                                                   link=res["link"]) for res in results])


google_tool = CustomGoogleSearchTool(
    name='Google Search Tool',
    description="Use this tool when user asks question that needs to look up contexts from the Internet ",
    api_wrapper=GoogleSearchAPIWrapper(
        google_api_key=env.GOOGLE_API_KEY,
        google_cse_id="e61c62a86e2b848fd",
        search_engine='Search Engine Basic'
    )
)

class AnswerWithSourceChain(LLMChain):
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE),
            HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)
        ]
    )
    llm = get_llm(model_name=ANSWERING_DEPLOYMENT,
                  temperature=0.8,
                  streaming=True,
                  max_new_tokens=1024)


class GoogleBasedTool(BaseTool):
    _instance = None
    chain = AnswerWithSourceChain()

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = GoogleBasedTool()
        return cls._instance

    name: str = "Internet Search"
    description: str = "This tool involves using the Internet to research the user's question and find more information that can help answer it. The decision maker should use this tool when they don't have the necessary knowledge to answer the question on their own, or when they want to verify or supplement their existing knowledge."
    args_schema: Type[BaseRequest] = BaseRequest

    def _run(self, **kwargs):
        message = self.chain.run(kwargs.get('human_message'))
        ai_message = Message(role=ASSISTANT, content=message).dict()
        ai_message.update({"token_num": 0})
        return ai_message
