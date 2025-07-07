from sentence_transformers import SentenceTransformer

model=SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text):
    embeddings = model.encode(text, normalize_embeddings=True)
    return embeddings