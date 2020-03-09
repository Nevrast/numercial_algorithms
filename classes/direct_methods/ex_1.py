import numpy as np

from classes.utils.utils import backward_substitution


def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    B = np.c_[A, b]
    for i in range(B.shape[0]):
        B[i] = B[i] - (B[i][i - 1] / B[i - 1][i - 1]) * B[i - 1]
    return B[:, :-1], B[:, -1:]


if __name__ == "__main__":
    A = np.array([[2, -1, 0, 0],
                  [-1, 2, -1, 0],
                  [0, -1, 2, -1],
                  [0, 0, -1, 2]], dtype=np.float)
    b = np.array([0, 0, 0, 5], dtype=np.float)
    x, B = gaussian_elimination(A=A, b=b)
    my_result = backward_substitution(A=x, b=B)
    builtin_result = np.linalg.solve(a=A, b=b)
    print(my_result == builtin_result)
    pass
