import numpy as np


def mae(y: np.ndarray, yhat: np.ndarray) -> float:
    """
    Mean absolute error.

    y, yhat: shape (n,), can be negative or positive; errors can point
    either direction.

    Return mean(|y - yhat|) over all n rows.
    """
    return np.mean(np.abs(y - yhat))
