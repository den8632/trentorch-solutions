import numpy as np


def bce_loss(y: np.ndarray, yhat: np.ndarray) -> float:
    """
    Binary cross-entropy loss.
    """
    loss = -(y * np.log(yhat) + (1 - y) * np.log(1 - yhat)).mean()
    return float(loss)
