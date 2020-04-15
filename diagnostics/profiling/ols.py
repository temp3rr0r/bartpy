import pandas as pd
import numpy as np

from bartpy.sklearnmodel import SklearnModel


def run(alpha, beta, n_trees, n_regressors, n_burn=50, n_samples=200, n_obsv=1000):
    b_true = np.random.uniform(-2, 2, size = n_regressors)
    x = np.random.normal(0, 1, size=n_obsv * n_regressors).reshape(n_obsv, n_regressors)
    X = pd.DataFrame(x)
    y = np.random.normal(0, 0.1, size=n_obsv) + np.array(X.multiply(b_true, axis = 1).sum(axis=1))
    model = SklearnModel(n_samples=n_samples,
                         n_burn=n_burn,
                         n_trees=n_trees,
                         alpha=alpha,
                         beta=beta,
                         n_jobs=1,
                         n_chains=1,
                         initializer=None,
                         store_acceptance_trace=False,
                         store_in_sample_predictions=False)
    model.fit(X, y)
    model.predict(X)


if __name__ == "__main__":
    model, x, y = run(0.95, 2., 200, 50, n_obsv=10000)
