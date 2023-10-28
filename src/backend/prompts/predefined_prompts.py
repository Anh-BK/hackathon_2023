STANDARD = """
Your task is help reader by answering their question extracted from the given context delimited by triple quotes.\ 
Instruction: Answer the question from the context. Remember to only answer if there are relevant information in the context.\ 
If you cannot find information in the text, just simply write \"The information is not found in the context.\"\n 
"""

SUMMARIZATION = """
- Summarization task: Summarize the context delimited by triple backticks. \ 
Then answer the question delimited by triple quotes. \ 
You should think step-by-step: 

Step 1: Extract the information that need to be summary from the question delimited by triple quotes and the history chat delimited by <>. \
Step 2: Find the relevant information in the given context delimited by triple backticks. \
Step 3: Summary the relevant information into 2-3 sentences. If the text does not contain relevant information,\ 
simply write \"Text not mentioned\". 
"""

REWRITE = """
Your task is to help reader in a conversation by re-writing the question\ 
to make it more clear. \n
Extract the relevant information from history conversation,\ 
then re-write the question. Let's think step-by-step. \n


History: <Question: Who is the president of the US in 2020? \n
Answer: Donald Trump.> \n 
Question: \"\"\"When was he born? \"\"\"

First, you need to read the question and the history. Then, to make the question to be more clear, \ 
people have to understand 'he' means 'Donald Trump'. So you need to replace 'he' by 'Donald Trump in the re-write question.\ 

Re-write question: When was Donald Trump born?

History: <Question: What does FPT stand for?\n 
Answer: FPT stands for Financing and Promoting Technology.>\n
Question: Summary the company's business aspect in 2010. 
Re-write question: Sumamry the business aspect of FPT in 2010. 

"""

EXTRACTION = """
- Extraction task: Your task is to answer the question of human delimited by triple quotes \ 
based on the context delimited by the triple backsticks and the history chat delimited by <>. \ 
If the information is not mentioned in the context, just simply write \"The information is not mentioned.\" \ 
""" 

INTERPRETATION = """
- New insight task: Your task is to provide a new perspective or new insights to reader about some documents.\ 
Given the context, explain the intended meaning of the extracted information.\ 
You should think step-by-step and only write out at the final output: 

Step 1: Summary the given context delimited by triple backsticks into 2-3 sentences, \ 
focusing on the aspects mentioned in the question delimited by triple quotes.\ 

Step 2: Generate new insights meaning of the summarized information to be the final output.\ 
The final answer should focus on the new insight. 

Context: ```The revenue of the company in 2016 is 20 million usd. At the end of 2020, the company reach 200 million usd of revenue and 50 million of profit.\ 
The number of employees increases from 100 people (only 10 women) in 2016 to 400 members (150 women) in 2020.```
History: <[]>
Question: \"\"\"What does the change of number of employees say about?\"\"\"

Answer: The number of employees of the company was significant, reaching 400 members in 2020. In 2016, there are only 10 female employees working in the company.\ 
This number increase rapidly from 2016 to 2020, reaching 150 female out of 400 employees in total. \n
"""
