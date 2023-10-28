from prompts.direct_qa import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
from prompts.comparision_prompts import COMPARISION_SYSTEM_TEMPLATE, COMPARISION_USER_TEMPLATE
from prompts.predefined_prompts import SUMMARIZATION, INTERPRETATION, EXTRACTION, STANDARD
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
    "comparition": {
        "system":COMPARISION_SYSTEM_TEMPLATE,
        "user":COMPARISION_USER_TEMPLATE,
    }
    # "predefined_prompt": {
    #     "system": PREDEFINED_ACTION_SYSTEM_TEMPLATE,
    #     "user": PREDEFINED_ACTION_HUMAN_TEMPLATE

    # }
}

PREDEFINED_ACTIONS = {
    "extraction": EXTRACTION,
    "interpretation": INTERPRETATION,
    "summarization": SUMMARIZATION,
    "standard": STANDARD
}

PROMPT = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(template=SYSTEM_TEMPLATE),
        HumanMessagePromptTemplate.from_template(template=HUMAN_TEMPLATE)
    ]
)
