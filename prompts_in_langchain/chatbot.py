import os
from langchain_openai import ChatOpenAI 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv('GROQ_API_KEY')
model= ChatOpenAI(
    model="llama3-8b-8192",  # or llama3-70b-8192
    openai_api_key=api_key,
    openai_api_base="https://api.groq.com/openai/v1"
)



chathistory=[
    SystemMessage(content="you are helpful ai assistant.")
]

while True:
    user_input= input("Enter you query\n")
    chathistory.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break

    result= model.invoke(user_input)
    chathistory.append(AIMessage(content=result.content))
    print(result.content)

print(chathistory)