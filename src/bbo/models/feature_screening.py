
import numpy as np

def ard_mask(lengths,thr):
    rel=lengths/lengths.max()
    return rel>thr
