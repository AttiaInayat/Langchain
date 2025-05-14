from langchain_openai import OpenAIEmbeddings # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

model= OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)

result=model.embed_query("what is github")
print(result)

docs=[
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result_doc= model.embed_documents(docs)
print(result_doc)