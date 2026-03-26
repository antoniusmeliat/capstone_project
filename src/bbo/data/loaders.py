import numpy as np
import json
import yaml
import os

def load_npy(path: str):
    return np.load(path)

def load_json(path: str):
    with open(path, 'r') as f:
        return json.load(f)

def load_yaml(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_xy(folder: str):
    X_path = os.path.join(folder, 'X.npy')
    Y_path = os.path.join(folder, 'Y.npy')
    X = np.load(X_path)
    Y = np.load(Y_path)
    return X, Y