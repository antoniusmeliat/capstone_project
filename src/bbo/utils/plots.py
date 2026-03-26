
# plots.py - Visualization utilities
import matplotlib.pyplot as plt
import numpy as np

def plot_ei_surface(X, EI):
    plt.scatter(X[:,0], X[:,1], c=EI, cmap='viridis')
    plt.colorbar(); plt.title('EI Surface'); plt.show()

def plot_convergence(Y):
    plt.plot(np.minimum.accumulate(Y)); plt.title('Best-so-far'); plt.show()
