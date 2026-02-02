from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read documents
with open("data/documents.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# Generate embeddings
embeddings = model.encode(documents)

# Save embeddings locally (simulating storage in Endee)
np.save("data/embeddings.npy", embeddings)
np.save("data/texts.npy", np.array(documents, dtype=object))

print("Documents ingested successfully.")
print(f"Total documents stored: {len(documents)}")
