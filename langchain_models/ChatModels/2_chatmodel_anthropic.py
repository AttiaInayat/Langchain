from langchain_anthropic import ChatAnthropic # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

model=ChatAnthropic(model='claude-3.5-sonnet')
result= model.invoke('capital of pakistan?')
print(result.content)