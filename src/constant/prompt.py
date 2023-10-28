from prompts.direct_qa import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
<<<<<<< HEAD
from prompts.predefined_prompts import SUMMARIZATION, INTEPRETATION, EXTRACTION
=======
from prompts.predefined_qa import PREDEFINED_ACTION_SYSTEM_TEMPLATE, PREDEFINED_ACTION_HUMAN_TEMPLATE
>>>>>>> 54b39fc804e34ea48e059081f710741024e13fc6
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
<<<<<<< HEAD
    # "predefined_prompt": {
    #     "system": PREDEFINED_ACTION_SYSTEM_TEMPLATE,
    #     "user": PREDEFINED_ACTION_HUMAN_TEMPLATE

    # }
}

PREDEFINED_ACTIONS = {
    "extraction": EXTRACTION,
    "interpretation": INTEPRETATION,
    "summarization": SUMMARIZATION
=======
    "predefined_prompt": {
        "system": PREDEFINED_ACTION_SYSTEM_TEMPLATE,
        "user": PREDEFINED_ACTION_HUMAN_TEMPLATE

    }
>>>>>>> 54b39fc804e34ea48e059081f710741024e13fc6
}

PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(template=SYSTEM_TEMPLATE),
        HumanMessagePromptTemplate.from_template(template=HUMAN_TEMPLATE)
    ]
)
