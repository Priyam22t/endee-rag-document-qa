from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load stored data
embeddings = np.load("data/embeddings.npy")
texts = np.load("data/texts.npy", allow_pickle=True)

# User question
question = input("Enter your question: ")

# Create question embedding
question_embedding = model.encode([question])[0]

# Cosine similarity
similarities = embeddings @ question_embedding / (
    norm(embeddings, axis=1) * norm(question_embedding)
)

# Get best match
best_index = similarities.argmax()

print("\nRetrieved Context:")
print(texts[best_index])

print("\nFinal Answer:")
print(
    f"{texts[best_index]}"
)
