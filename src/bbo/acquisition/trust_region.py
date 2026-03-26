
# trust_region.py - Simple trust region handling for BO
import numpy as np

def trust_region(center, radius, n_candidates):
    d = center.shape[0]
    samples = center + np.random.uniform(-radius, radius, size=(n_candidates, d))
    return np.clip(samples, 0.0, 1.0)
