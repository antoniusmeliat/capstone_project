
# ucb.py - Upper Confidence Bound acquisition function
import numpy as np

def upper_confidence_bound(mean, std, kappa=2.0):
    return mean + kappa * std
