import numpy as np
import copy


def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    B = np.c_[A, b]
    for i in range(B.shape[0]):
        B[i] = B[i] - (B[i][i - 1] / B[i - 1][i - 1]) * B[i - 1]
    return B[:, :-1], B[:, -1:]


def backward_substitution(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = b.shape[0]
    x = np.zeros_like(b)

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(calculate_row(row=A[i], x=x)[i + 1:] if i != n - 1 else [])) / A[i, i]
        print(A[i, i])

    return x.flat


def calculate_row(row: np.ndarray, x: np.ndarray) -> np.ndarray:
    row = copy.deepcopy(row)
    for index, x_value in enumerate(x):
        if x_value != 0:
            row[index] *= x_value
    return row


if __name__ == "__main__":
    A = np.array([[2, -1, 0, 0],
                  [-1, 2, -1, 0],
                  [0, -1, 2, -1],
                  [0, 0, -1, 2]], dtype=np.float)
    b = np.array([0, 0, 0, 5], dtype=np.float)
    x, B = gaussian_elimination(A=A, b=b)
    my_result = backward_substitution(A=x, b=B)
    builtin_result = np.linalg.solve(a=A, b=b)
    assert all(my_result == builtin_result)