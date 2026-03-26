
import numpy as np, json

def load_npy(p): return np.load(p)
def save_npy(p,a): np.save(p,a)

def load_json(p):
    with open(p) as f: return json.load(f)
def save_json(p,o):
    with open(p,'w') as f: json.dump(o,f,indent=4)
