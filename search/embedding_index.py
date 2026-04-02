from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text):
    return model.encode(text)


def build_index(file_index):

    vectors = []

    for f in file_index:
        vec = embed(f["snippet"])
        vectors.append((vec, f))

    return vectors

def search(query, index, top_k=3):

    q_vec = embed(query)

    scored = []

    for vec, f in index:
        score = np.dot(q_vec, vec)
        scored.append((score, f))

    scored.sort(reverse=True)

    return [f for _, f in scored[:top_k]]
