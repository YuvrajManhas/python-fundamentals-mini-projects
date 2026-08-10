from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("sentences.txt", "r", encoding="utf-8") as file:
    sentences = [line.strip() for line in file if line.strip()]

embeddings = model.encode(sentences)

query = input("Enter a sentence: ")
query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    embeddings
)[0]

results = list(zip(sentences, similarities))

results.sort(key = lambda x : x[1], reverse = True)

print("\nMost similar sentences:\n")

threshold = 0.5

for sentence, score in results:
    if score >= threshold:
        print(f"{score:.4f} - {sentence}")