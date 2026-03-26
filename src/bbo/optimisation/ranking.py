
# ranking.py - Rank candidate points for BO
import numpy as np

def rank_candidates(scores, top_k=5):
    idx = np.argsort(scores)[::-1]  # descending
    return idx[:top_k]
