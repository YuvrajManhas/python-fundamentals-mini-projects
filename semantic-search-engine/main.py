import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

with open("data/documents.txt", "r", encoding="utf-8") as file:
    documents = [line.strip() for line in file if line.strip()]


model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    documents,
    convert_to_numpy = True
)

faiss.normalize_L2(embeddings)
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

query = input("\nEnter your search Query: ")

query_embedding = model.encode(
    [query],
    convert_to_numpy = True
)

faiss.normalize_L2(query_embedding)

k = 3
scores, indices = index.search(query_embedding, k)

print("\nSearch Results:\n")

for rank, (score, index_position) in enumerate(
    zip(scores[0], indices[0]),
    start = 1
):
    print(f"{rank}. {documents[index_position]}")
    print(f"    Similarity: {score:.4f}\n")

