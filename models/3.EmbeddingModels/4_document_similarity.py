from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions = '300'
)

documents = [
    "Virat kohli is an indian cricketer known for his aggressive battinga nd leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demenoar and finishing skills",
    "Sachin Tendulkar, also known as the 'God of cricket', holder many batting Records.",
    "Rohit sharma is known for his elegant batting and record-breaking double centuries",
    "Jasprit Bumrah is an Indian Fast bowler known for his unorthodox action and yourkeres"
]

query = 'tell me about virat kohli'

document_embedding = embedding.embed_documents(documents)

query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings],document_embedding)[0]

index , score = sorted(list(enumerate(scores)) , key = lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is:",score)