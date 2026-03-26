import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def scale_minmax(X):
    scaler = MinMaxScaler()
    return scaler.fit_transform(X), scaler

def scale_standard(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X), scaler

def remove_duplicates(X, Y):
    unique, idx = np.unique(X, axis=0, return_index=True)
    return X[idx], Y[idx]

def clip_bounds(X, bounds):
    Xc = X.copy()
    for dim, (lo, hi) in bounds.items():
        Xc[:, dim] = np.clip(Xc[:, dim], lo, hi)
    return Xc