import numpy as np


def backward_substitution(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = b.shape[0]
    x = np.zeros_like(b)

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(calculate_row(row=A[i], x=x)[i + 1:] if i != n - 1 else [])) / A[i, i]

    return x


def calculate_row(row: np.ndarray, x: np.ndarray) -> np.ndarray:
    for index, x_value in enumerate(x):
        if x_value != 0:
            row[index] *= x_value
    return row
