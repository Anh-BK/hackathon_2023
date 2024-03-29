import os
from dotenv import load_dotenv

class ENV:
    load_dotenv()
    API_HOST = os.environ.get("API_HOST", "0.0.0.0")
    API_PORT = os.environ.get("API_PORT", 8002)
    MONGODB_HOST = os.environ.get("MONGODB_HOST", "0.0.0.0")
    MONGODB_PORT = os.environ.get("MONGODB_PORT", 27017)

    ### Azure OpenAI ###
    OPENAI_KEY = os.environ.get("OPENAI_KEY", "")
    GOOGLE_API_KEY = os.environ.get("GOOGLE_KEY", "")
    AZ_OAI_VERSION = os.environ.get("AZ_OAI_VERSION", "2023-03-15-preview")
    AZ_OAI_BASE = os.environ.get("AZ_OAI_BASE", "")
    AZ_OAI_MODEL = os.environ.get("AZ_OAI_MODEL", "")
    ANSWERING_MODEL = os.environ.get("ANSWERING_MODEL", AZ_OAI_MODEL)
