
# gp.py - Gaussian Process surrogate implementation

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel

class GPModel:
    def __init__(self, nu=2.5, n_restarts=10, standardize_y=True):
        self.kernel = Matern(nu=nu) + WhiteKernel()
        self.model = GaussianProcessRegressor(
            kernel=self.kernel,
            n_restarts_optimizer=n_restarts,
            normalize_y=standardize_y
        )

    def fit(self, X, Y):
        self.model.fit(X, Y)

    def predict(self, X):
        mean, std = self.model.predict(X, return_std=True)
        return mean, std
