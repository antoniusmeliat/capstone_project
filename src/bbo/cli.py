
# cli.py - Command-line interface
import argparse
from .io import load_npy

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data', required=True)
    args=p.parse_args()
    X=load_npy(args.data)
    print('Loaded shape:', X.shape)

if __name__=='__main__': main()
