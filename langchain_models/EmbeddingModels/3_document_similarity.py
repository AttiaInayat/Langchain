from langchain_huggingface import HuggingFaceEmbeddings # type: ignore
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

doc_emb= embedding.embed_documents(documents)
query_emb= embedding.embed_query(query)

scores= cosine_similarity([query_emb],doc_emb)[0]
print(scores)
index,score= sorted(list(enumerate(scores)),key=lambda x: x[1])[-1]
print(documents[index])
print(score)
