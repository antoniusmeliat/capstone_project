
# ei.py - Expected Improvement acquisition function
import numpy as np
from scipy.stats import norm

def expected_improvement(mean, std, best, xi=0.01):
    z = (mean - best - xi) / (std + 1e-9)
    return (mean - best - xi) * norm.cdf(z) + std * norm.pdf(z)
