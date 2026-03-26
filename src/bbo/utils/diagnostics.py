
# diagnostics.py - Diagnostics utilities
import numpy as np

def summarize_array(arr): return {
    'min': float(arr.min()), 'max': float(arr.max()),
    'mean': float(arr.mean()), 'std': float(arr.std()) }

def check_nan(arr): return np.isnan(arr).sum()
