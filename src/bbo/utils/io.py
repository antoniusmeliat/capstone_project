
# io.py - File input/output helpers
import numpy as np, json, yaml

def load_npy(path): return np.load(path)
def save_npy(path, arr): np.save(path, arr)

def load_json(path): return json.load(open(path))
def save_json(path,obj): json.dump(obj, open(path,'w'), indent=4)

def load_yaml(path): return yaml.safe_load(open(path))
def save_yaml(path,obj): yaml.safe_dump(obj, open(path,'w'))
