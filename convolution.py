import numpy as np


def convolve_1d(x, h):
    """Full 1D convolution of signal x with kernel h, from scratch.
    Output length is len(x) + len(h) - 1 (the 'full' overlap)."""
    x = np.asarray(x, dtype=float)
    h = np.asarray(h, dtype=float)
    n_out = len(x) + len(h) - 1
    y = np.zeros(n_out)

    h_flipped = h
    # Pad x with (len(h)-1) zeros on each side so the kernel can hang off both ends
    pad = len(h) - 1
    x_padded = np.concatenate([np.zeros(pad), x, np.zeros(pad)])

    for n in range(n_out):
        window = x_padded[n : n + len(h)]   # the slice the kernel sits over
        y[n] = np.dot(window, h_flipped)
    return y


def moving_average(x, k):
    """k-point moving average — convolution with a uniform kernel."""
    kernel = np.ones(k) / k
    return convolve_1d(x, kernel)


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    h = np.array([1, 0, -1], dtype=float)   # asymmetric ON PURPOSE — exposes the flip

    mine = convolve_1d(x, h)
    ref  = np.convolve(x, h, mode="full")

    print("mine:", mine)
    print("ref :", ref)
    print("match:", np.allclose(mine, ref))