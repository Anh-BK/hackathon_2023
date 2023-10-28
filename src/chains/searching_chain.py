import re

from typing import List
from chains.query_extractor import QueryExtractorLangchain
from schema import Message
from tools.content_retrieval import retrieval_tool
from tools.google_based_qa import google_tool, AnswerWithSourceChain
from prompts.query_extractor import HUMAN_TEMPLATE
from constant.prompt import PREDEFINED_ACTIONS
from utils.helper import split_bullet_point

class OnlineSearch(QueryExtractorLangchain):
    def __init__(self, *args, **kwargs):
        super(OnlineSearch, self).__init__(*args, **kwargs)
        self.composer = AnswerWithSourceChain()
        self.max_tokens = 8192
        self.max_gen_tokens = 1024
        self.detailed_search = True
        self.num_queries = 5

    def run(self, history: List[Message] = [], **kwargs):
        kwargs["context"] = kwargs.get("context", "")
        task_name = kwargs.get("task", "standard")
        kwargs["task_requirement"] = PREDEFINED_ACTIONS.get[task_name]

        param_query_extractor = {key: value for key, value in kwargs.items() if key not in ['streaming', 'callbacks']}
        text_results = super().run(HUMAN_TEMPLATE, history, streaming=False, **param_query_extractor)
        search_results = text_results["content"].replace('"', '').split("\n")
        queries = list(map(split_bullet_point, search_results))

        composer_kwargs = {
            "question": '{question}\n{context}\nrequirements:{task_requirement}'.format(**kwargs),
            "sources": ""
        }

        tool = google_tool
        tool.num_results = 1
        if self.detailed_search:
            tool = retrieval_tool
        for query in queries[:self.num_queries]:
            searched_results = tool.run(query, num_results=max(6//len(queries), 1))
            composer_kwargs["sources"] += searched_results

        pattern = r"Content: (.*?)\nSource: (.*?)\n\n"
        reference = ""
        format_source = ""
        for (idx, source) in enumerate(re.findall(pattern, composer_kwargs["sources"], re.DOTALL)):
            reference += f"[{idx + 1}]" + " Source: " + source[1] + "\n"
            format_source += "Content: " + source[0] + "\n" + f"[{idx + 1}]" + " Source: " + source[1] + "\n\n"
        composer_kwargs["sources"] = format_source
        citation = "**Citations:**\n" + reference
        print(composer_kwargs)
        ai_message = self.composer.predict(**composer_kwargs, callbacks=kwargs.get("callbacks"))
        return ai_message, citation

if __name__ == '__main__':
    chain = OnlineSearch()
    history = [
        {
            "role": "user",
            "content": "what is ROI index?"
        },
        {
            "role": "assistant",
            "content": "ROI stands for Return on Investment. It is a financial metric that measures the profitability of an investment relative to its cost. The ROI index is a way of expressing the ROI in percentage terms, making it easier to compare different investments."
        }
    ]
    answer = chain.run(history=history, question="What is Index fund?", context="")
    print(f"Codevista's answer: {answer}")
