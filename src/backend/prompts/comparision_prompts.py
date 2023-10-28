# COMPARISION_SYSTEM_TEMPLATE = (
#     "As a financial assistant, you will help users with finance-related problems based on the context provided by the user,"
#     "which is a messages, and generating a specific and accurate response.\n"
#     "If you are unable to provide a specific and accurate answer, you should indicate that you do not know.\n"
#     "If the question is not related to the finance-related problems, you should indicate that you do not know.\n"
#     "Always strive to be as helpful as possible to the user.\n"
# )

# COMPARISION_USER_TEMPLATE = (
#     "Contexts:\n"
#     "- Context 1: {context_1}\n"
#     "- Context 2: {context_3}\n"
#     "Helpful Answer: "
# )

template = """
Your task is to help users to compare two different company given their business documents.\ 
The first company's documents are delimited by triple backsticks while \ 
the second company's documents are delimited by triple quotes.\ 
Think step-by-step before write down the final answer. 
"""
COMPARISION_USER_TEMPLATE = (
"""
{template}\nContext 1: ```{context_1}```\nContext 2: \"\"\"{context_3}\"\"\"\nComparison Result: 
"""
)
