from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
"""
Additional Mode to the game

Librarian

Librarian is a part that where Semantic Search Functionality has been added

Librarian Mode will have 3 Main game plays 

1 - Librarian Clerk

This game mode is only for semantic search where users will be given a riddle and prompt area where they will be able to search for documents
Depends on the level strength/diffuculty provided document context might be relavent information only or completely missing
User needs to find a way to answer to a riddle or question by searching through provided document by prompting and thiking.

2 - Librarian technicians

This game mode will have LLM included where it will help and time to time protect the information to be accessed directly. User needs to combine his knowledge from Warden Levels
as well as Librarian Clerk level to accomplish tasks here. Depends on the diffuculties there will be different guards such as in the Warden levels

3 - Disinformation

This part is consist of deliberatly poisoned data. This part works by providing extra data which has close similarity with the prompt attack senteces, keywords.
Those information will be inserted inside the vector clusters to protect actual data by providing some honeypot layer on the top of it.
This part should be the hardest part where all Librarian and Warden modes are combined. 

"""
openai_api_key = os.getenv("OPENAPI_KEY","")
os.environ["OPENAI_API_KEY"] = openai_api_key
chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

"""
Will include this part later.
"""