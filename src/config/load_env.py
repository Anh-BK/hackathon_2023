import os
from dotenv import load_dotenv

class ENV:
    load_dotenv()
    API_HOST = os.environ.get("API_HOST", "0.0.0.0")
    API_PORT = os.environ.get("API_PORT", 8000)
    MONGODB_HOST = os.environ.get("MONGODB_HOST", "0.0.0.0")
    MONGODB_PORT = os.environ.get("MONGODB_PORT", 27017)

    ### Azure OpenAI ###
    OPENAI_KEY = os.environ.get("OPENAI_KEY", "")
    AZ_OAI_VERSION = os.environ.get("AZ_OAI_VERSION", "2023-03-15-preview")
    AZ_OAI_BASE = os.environ.get("AZ_OAI_BASE", "https://codevista-opai.openai.azure.com/")
    AZ_OAI_MODEL = os.environ.get("AZ_OAI_MODEL", "codevista-gpt35-turbo")
    ANSWERING_MODEL = os.environ.get("ANSWERING_MODEL", AZ_OAI_MODEL)
