from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')
result=model.invoke('capital of pakistan')
print(result.content)