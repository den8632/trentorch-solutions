import numpy as np


def max_pool_strided(matrix: np.ndarray, k: int, s: int) -> np.ndarray:
    """
    2D max pooling with independent kernel size k and stride s, no padding.

    matrix: shape (H, W).
    k: window size (height and width). s: stride, can differ from k.

    Output shape is (floor((H-k)/s)+1, floor((W-k)/s)+1). Cell (i, j) is the
    max over the window with top-left corner (i*s, j*s), size k x k. Any
    trailing rows/columns that don't fill a full window are dropped, not
    padded.
    """
    H, W = matrix.shape
    out_h = (H - k) // s + 1
    out_w = (W - k) // s + 1
    out = np.empty((out_h, out_w), dtype=matrix.dtype)
    for i in range(out_h):
        for j in range(out_w):
            out[i, j] = matrix[i*s:i*s+k, j*s:j*s+k].max()
    return out
