
# neural_net.py - Simple MLP surrogate for BO

import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import BaggingRegressor

class NeuralNetModel:
    def __init__(self, hidden=(128,128), lr=1e-3, weight_decay=1e-4, epochs=200, ensemble=4):
        base = MLPRegressor(
            hidden_layer_sizes=hidden,
            learning_rate_init=lr,
            alpha=weight_decay,
            max_iter=epochs,
            solver='adam'
        )
        self.model = BaggingRegressor(base, n_estimators=ensemble)

    def fit(self, X, Y):
        self.model.fit(X, Y)

    def predict(self, X):
        preds = np.array([est.predict(X) for est in self.model.estimators_])
        mean = preds.mean(axis=0)
        std = preds.std(axis=0)
        return mean, std
