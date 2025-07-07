from sklearn.metrics.pairwise import cosine_similarity
from model.embedder import get_embeddings

TARGET_TOPICS = [
    "machine learning engineer",
    "android developer",
    "react native developer",
    "tensorflow internship",
    "computer vision project",
    "ai hackathon",
]

# Precompute interest vectors
target_embeddings = [get_embeddings(topic) for topic in TARGET_TOPICS]

def is_relevant(job_description: str, threshold= 0.6):
    job_vector= get_embeddings(job_description)
    scores=[cosine_similarity([job_vector], [target])[0][0] for target in target_embeddings]
    max_score = max(scores)
    return max_score >= threshold, max_score
