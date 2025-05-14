from langchain_huggingface import HuggingFaceEmbeddings # type: ignore

docs=[
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
vector=embedding.embed_documents(docs)
print(vector)