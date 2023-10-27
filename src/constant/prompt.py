from prompts.direct_qa import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
from prompts.predefined_prompts import SUMMARIZATION, INTEPRETATION, EXTRACTION
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


PROMPT_TYPES = {
    "basic": {
        "system": SYSTEM_TEMPLATE,
        "user": HUMAN_TEMPLATE,
    },
    # "predefined_prompt": {
    #     "system": PREDEFINED_ACTION_SYSTEM_TEMPLATE,
    #     "user": PREDEFINED_ACTION_HUMAN_TEMPLATE

    # }
}

PREDEFINED_ACTIONS = {
    "extraction": EXTRACTION,
    "interpretation": INTEPRETATION,
    "summarization": SUMMARIZATION
}

PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(template=SYSTEM_TEMPLATE),
        HumanMessagePromptTemplate.from_template(template=HUMAN_TEMPLATE)
    ]
)
