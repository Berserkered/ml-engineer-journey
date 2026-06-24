import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Known ground truth: y = 3x + 2 + noise. We should recover w≈3, b≈2.
m = 100
X = rng.uniform(-5, 5, size=(m, 1))           # (m, 1) — kept 2D on purpose
true_w, true_b = 3.0, 2.0
y = true_w * X[:, 0] + true_b + rng.normal(0, 1.0, size=m)   # (m,)


def fit_linear_regression(X, y, lr=0.01, n_iters=1000):
    m, n = X.shape
    w = np.zeros(n)        # (n,)
    b = 0.0
    history = []

    for _ in range(n_iters):
        y_hat = X @ w + b
        error = y_hat - y  # (m,)
        loss  = (1 / m) * np.sum(error ** 2)

        dw = (1 / m) * X.T @ error
        db = (1 / m) * np.sum(error)

        w -= lr * dw
        b -= lr * db

        history.append(loss)
    return w, b, history


w, b, history = fit_linear_regression(X, y)
print(f"recovered w={w}, b={b:.3f}")
plt.plot(history); plt.xlabel("iteration"); plt.ylabel("MSE"); plt.show()