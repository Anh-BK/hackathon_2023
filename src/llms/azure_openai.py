from typing import List
from langchain.chat_models import AzureChatOpenAI

class CustomAzureOpenAI(AzureChatOpenAI):
    stop: List[str] = None
    @property
    def _invocation_params(self):
        params = super()._invocation_params
        # fix InvalidRequestError: logprobs, best_of and echo parameters are not available on gpt-35-turbo model.
        params.pop('logprobs', None)
        params.pop('best_of', None)
        params.pop('echo', None)
        #params['stop'] = self.stop
        return params