from langchain_openai import ChatOpenAI # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
model= ChatOpenAI(model='gpt-4',temperature=1.5, max_completion_tokens=10)
result= model.invoke('Which is the capital of pakistan')
print(result.content)