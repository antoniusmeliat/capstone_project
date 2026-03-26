
# proposer.py - Candidate proposal module for BO
import numpy as np
from .ei import expected_improvement
from .ucb import upper_confidence_bound
from .trust_region import trust_region

def propose_next(X, Y, surrogate, cfg):
    mean, std = surrogate.predict(X)

    if cfg.get('strategy','ei') == 'ei':
        acq = expected_improvement(mean, std, np.min(Y), cfg.get('xi',0.01))
    else:
        acq = upper_confidence_bound(mean, std, cfg.get('kappa',2.0))

    idx = np.argmax(acq)
    return X[idx], acq[idx]
