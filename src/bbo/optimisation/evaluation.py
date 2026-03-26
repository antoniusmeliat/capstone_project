
# evaluation.py - Evaluate BO performance metrics
import numpy as np

def rmse(pred, true):
    return np.sqrt(((pred-true)**2).mean())

def mae(pred, true):
    return np.abs(pred-true).mean()

def best_so_far(Y):
    return np.minimum.accumulate(Y)
