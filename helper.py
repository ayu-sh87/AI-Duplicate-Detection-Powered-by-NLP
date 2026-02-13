from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load SBERT
sbert = SentenceTransformer('all-MiniLM-L6-v2')

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model expects:", model.n_features_in_)


def create_features(q1, q2):
    # embeddings
    emb1 = sbert.encode(q1)
    emb2 = sbert.encode(q2)

    emb1 = np.array(emb1)
    emb2 = np.array(emb2)

    # feature engineering (same as notebook)
    abs_diff = np.abs(emb1 - emb2)
    mult = emb1 * emb2
    sim = cosine_similarity([emb1], [emb2])[0][0]

    # final feature vector
    features = np.hstack((
        emb1,
        emb2,
        abs_diff,
        mult,
        sim
    ))

    features = features.reshape(1, -1)

    return features
