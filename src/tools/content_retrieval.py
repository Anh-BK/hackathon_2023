import requests
import tiktoken

from bs4 import BeautifulSoup
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate)

from config.load_env import ENV
from llms.azure_openai import CustomAzureOpenAI
from llms import get_llm
from tools.google_based_qa import google_tool, AnswerWithSourceChain

env = ENV()
ANSWERING_DEPLOYMENT = env.ANSWERING_MODEL
encoding = tiktoken.get_encoding("cl100k_base")
human_template = "Question: {question}\nHTML Document: {doc}"


class ContentRetrievalChain(LLMChain):
    prompt = ChatPromptTemplate.from_messages(
        [SystemMessagePromptTemplate.from_template(
            "When provided with a question and a HTML document, generate a concise summary of the document's content "
            "that directly addresses the question."),
            HumanMessagePromptTemplate.from_template(human_template)
        ])
    # llm = CustomAzureOpenAI(deployment_name=ANSWERING_DEPLOYMENT,
    #                         openai_api_key=OPENAI_API_KEY,
    #                         openai_api_base=API_BASE,
    #                         openai_api_version=API_VERSION,
    #                         temperature=0,
    #                         max_tokens=256)
    llm = get_llm(model_name=ANSWERING_DEPLOYMENT, temperature=0, max_new_tokens=256)
    list_link = []

    def run(self, question: str, num_results: int) -> str:
        results = google_tool.api_wrapper.results(query=question, num_results=num_results)
        results = list(filter(lambda x: True if x.get("snippet") is not None else False, results))
        source_template = 'Content: {content}\nSource: [{title}]({link})'

        out_str = ""
        for res in results:
            if res["link"] in self.list_link:
                print(f'{res["link"]} is already in use.')
                continue
            self.list_link.append(res["link"])
            response = requests.get(res['link'])
            soup = BeautifulSoup(response.content, "html.parser")
            num_tokens = len(encoding.encode(human_template.format(question=question, doc=soup.get_text())))
            if num_tokens < 8192 - 256:
                summary = self.predict(question=question, doc=soup.get_text())
                out_str += source_template.format(content=summary,
                                                  title=res["title"],
                                                  link=res["link"])
            else:
                print(f"Cannot access ", res["link"])
                out_str += source_template.format(content=res["snippet"],
                                                  title=res["title"],
                                                  link=res["link"])

            out_str += "\n\n"

        return out_str


retrieval_tool = ContentRetrievalChain()

# if __name__ == "__main__":
#     # chain = ContentRetrievalChain()
#
#     chain = AnswerWithHTMLDocs()
#
#     out = chain.run("what is Mojo Programming Language?")
#
#     print(out)
