from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id= 'google/flan-t5-small',
    task='text-generation'
)

model= ChatHuggingFace(llm =llm)
result=model.invoke("What is the capital of pakistan")
print(result.content)