from llms.azure_openai import CustomAzureOpenAI
from config.load_env import ENV

env = ENV()

OPENAI_API_KEY = env.OPENAI_KEY
API_VERSION = env.AZ_OAI_VERSION
API_BASE = env.AZ_OAI_BASE

def get_llm(model_name: str,
            temperature: float = 0,
            max_new_tokens: int = 1024,
            streaming: bool = False
            ):
    model = CustomAzureOpenAI(deployment_name=model_name,
                              openai_api_key=OPENAI_API_KEY,
                              openai_api_base=API_BASE,
                              openai_api_version=API_VERSION,
                              temperature=temperature,
                              max_tokens=max_new_tokens,
                              streaming=streaming
                              )
    return model
