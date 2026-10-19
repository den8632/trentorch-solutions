import numpy as np


def conv1d(x: np.ndarray, kernel: np.ndarray, mode: str) -> np.ndarray:
    """
    1D cross-correlation ("convolution" in the deep-learning sense: the
    kernel is NOT flipped) with "valid" or "same" zero padding.

    x: shape (n,). kernel: shape (k,), k odd. mode: "valid" or "same".

    "valid": no padding, output length n - k + 1.
    "same": zero-pad x by k // 2 on each side first, output length n.

    Slide the kernel across the (possibly padded) signal without flipping
    it, taking sum(window * kernel) at each position.
    """
    if x.ndim != 1 or kernel.ndim != 1:
        raise ValueError("x and kernel must be 1D")
    if kernel.size == 0 or kernel.size % 2 == 0:
        raise ValueError("kernel must have a positive odd length")

    if mode == "valid":
        signal = x
    elif mode == "same":
        pad = kernel.size // 2
        signal = np.pad(x, (pad, pad), mode="constant")
    else:
        raise ValueError("mode must be 'valid' or 'same'")

    if signal.size < kernel.size:
        return np.array([], dtype=np.result_type(x, kernel, float))

    out = np.empty(signal.size - kernel.size + 1,
                   dtype=np.result_type(x, kernel, float))
    for i in range(out.size):
        out[i] = np.sum(signal[i:i + kernel.size] * kernel)

    return out
