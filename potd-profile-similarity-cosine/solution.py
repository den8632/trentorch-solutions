import numpy as np


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """
    Cosine similarity between two vectors.

    u, v: shape (d,).

    Return (u . v) / (||u|| * ||v||). If either vector is all zeros (norm
    0), return 0.0 instead of dividing by zero.
    """
    u_norm = np.linalg.norm(u)
    v_norm = np.linalg.norm(v)

    if u_norm == 0 or v_norm == 0:
        return 0.0

    return float(np.dot(u, v) / (u_norm * v_norm))
