
from scipy.stats import qmc

def sobol(n,d): return qmc.Sobol(d).random(n)

def lhs(n,d): return qmc.LatinHypercube(d).random(n)
