from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np


Array = np.ndarray


def householder_vector(x: Array) -> tuple[Array, float]:
    """Return v and beta for H = I - beta v v^T, following textbook Alg. 3.2.1."""
    x = np.asarray(x, dtype=float)
    n = x.size
    if n == 0:
        return np.array([], dtype=float), 0.0

    v = np.zeros(n, dtype=float)
    v[0] = 1.0
    sigma = float(np.dot(x[1:], x[1:]))

    if sigma == 0.0:
        return v, 0.0

    alpha = float(np.sqrt(x[0] * x[0] + sigma))
    if x[0] <= 0.0:
        v0 = x[0] - alpha
    else:
        v0 = -sigma / (x[0] + alpha)

    v[1:] = x[1:] / v0
    beta = 2.0 * v0 * v0 / (sigma + v0 * v0)
    return v, float(beta)


def householder_qr_compact(A: Array) -> tuple[Array, Array]:
    """Compute a compact Householder QR factorization of a full column rank matrix."""
    A = np.asarray(A, dtype=float)
    if A.ndim != 2:
        raise ValueError("A must be a matrix")

    m, n = A.shape
    if m < n:
        raise ValueError("Householder least squares requires m >= n")

    qr = A.copy()
    beta = np.zeros(n, dtype=float)

    for j in range(n):
        v, beta_j = householder_vector(qr[j:, j])
        beta[j] = beta_j
        if beta_j != 0.0:
            qr[j:, j:] -= beta_j * np.outer(v, v @ qr[j:, j:])
        if j + 1 < m:
            qr[j + 1 :, j] = v[1:]

    return qr, beta


def apply_q_transpose(qr: Array, beta: Array, b: Array) -> Array:
    """Apply Q^T to b using the compact Householder factors."""
    qr = np.asarray(qr, dtype=float)
    beta = np.asarray(beta, dtype=float)
    y = np.asarray(b, dtype=float).copy()

    if y.ndim != 1:
        raise ValueError("b must be a vector")
    if y.size != qr.shape[0]:
        raise ValueError("b length must match the number of rows of A")

    m, n = qr.shape
    for j in range(n):
        v = np.empty(m - j, dtype=float)
        v[0] = 1.0
        if j + 1 < m:
            v[1:] = qr[j + 1 :, j]
        y[j:] -= beta[j] * v * float(v @ y[j:])

    return y


def solve_upper_triangular(R: Array, b: Array, zero_tol: float = 0.0) -> Array:
    """Back substitution for an upper triangular system."""
    R = np.asarray(R, dtype=float)
    b = np.asarray(b, dtype=float)
    n = b.size

    if R.shape != (n, n):
        raise ValueError("R must be square and compatible with b")

    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        pivot = R[i, i]
        if abs(pivot) <= zero_tol:
            raise np.linalg.LinAlgError("singular or rank-deficient triangular factor")
        x[i] = (b[i] - R[i, i + 1 :] @ x[i + 1 :]) / pivot
    return x


def qr_least_squares(A: Array, b: Array, zero_tol: float = 0.0) -> Array:
    """Solve min ||Ax-b||_2 by Householder QR."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or b.ndim != 1:
        raise ValueError("A must be a matrix and b must be a vector")
    if A.shape[0] != b.size:
        raise ValueError("A and b have incompatible dimensions")

    _, n = A.shape
    qr, beta = householder_qr_compact(A)
    y = apply_q_transpose(qr, beta, b)
    R = np.triu(qr[:n, :n])
    try:
        return solve_upper_triangular(R, y[:n], zero_tol=zero_tol)
    except np.linalg.LinAlgError:
        # In numerically rank-deficient cases, keep the QR reduction and solve
        # the resulting triangular least-squares problem in the minimum-norm sense.
        x, *_ = np.linalg.lstsq(R, y[:n], rcond=None)
        return x


def qr_solve(A: Array, b: Array, zero_tol: float = 0.0) -> Array:
    """Solve a square linear system Ax=b by Householder QR."""
    A = np.asarray(A, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("qr_solve requires a square matrix")
    return qr_least_squares(A, b, zero_tol=zero_tol)


def solve_by_qr(A: Array, b: Array, zero_tol: float = 0.0) -> Array:
    """Use QR for square systems and full-column-rank least squares problems."""
    A = np.asarray(A, dtype=float)
    if A.shape[0] == A.shape[1]:
        return qr_solve(A, b, zero_tol=zero_tol)
    return qr_least_squares(A, b, zero_tol=zero_tol)


def gauss_no_pivoting(A: Array, b: Array) -> Array:
    A = np.asarray(A, dtype=float).copy()
    b = np.asarray(b, dtype=float).copy()
    n = b.size

    for k in range(n - 1):
        if A[k, k] == 0.0:
            raise np.linalg.LinAlgError("zero pivot")
        for i in range(k + 1, n):
            multiplier = A[i, k] / A[k, k]
            A[i, k:] -= multiplier * A[k, k:]
            b[i] -= multiplier * b[k]

    return solve_upper_triangular(A, b)


def gauss_partial_pivoting(A: Array, b: Array) -> Array:
    A = np.asarray(A, dtype=float).copy()
    b = np.asarray(b, dtype=float).copy()
    n = b.size

    for k in range(n - 1):
        pivot_row = k + int(np.argmax(np.abs(A[k:, k])))
        if A[pivot_row, k] == 0.0:
            raise np.linalg.LinAlgError("zero pivot")
        if pivot_row != k:
            A[[k, pivot_row], :] = A[[pivot_row, k], :]
            b[[k, pivot_row]] = b[[pivot_row, k]]
        for i in range(k + 1, n):
            multiplier = A[i, k] / A[k, k]
            A[i, k:] -= multiplier * A[k, k:]
            b[i] -= multiplier * b[k]

    return solve_upper_triangular(A, b)


def cholesky_solve(A: Array, b: Array) -> Array:
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    L = np.linalg.cholesky(A)
    y = np.linalg.solve(L, b)
    return np.linalg.solve(L.T, y)


def ldlt_solve(A: Array, b: Array) -> Array:
    A = np.asarray(A, dtype=float).copy()
    b = np.asarray(b, dtype=float)
    n = A.shape[0]

    v = np.zeros(n, dtype=float)
    for j in range(n):
        for i in range(j):
            v[i] = A[j, i] * A[i, i]
        A[j, j] -= A[j, :j] @ v[:j]
        if A[j, j] <= 0.0:
            raise np.linalg.LinAlgError("nonpositive LDLT pivot")
        for k in range(j + 1, n):
            A[k, j] = (A[k, j] - A[k, :j] @ v[:j]) / A[j, j]

    y = np.zeros(n, dtype=float)
    for i in range(n):
        y[i] = b[i] - A[i, :i] @ y[:i]

    z = y / np.diag(A)

    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = z[i] - A[i + 1 :, i] @ x[i + 1 :]
    return x


def build_first_chapter_systems(seed: int = 42) -> list[tuple[str, Array, Array, Array]]:
    systems: list[tuple[str, Array, Array, Array]] = []

    n = 84
    A = (
        np.diag(np.full(n, 6.0))
        + np.diag(np.full(n - 1, 8.0), -1)
        + np.diag(np.full(n - 1, 1.0), 1)
    )
    b = np.full(n, 15.0)
    b[0] = 7.0
    b[-1] = 14.0
    systems.append(("84-order nonsymmetric tridiagonal", A, b, np.ones(n)))

    n = 100
    A = (
        np.diag(np.full(n, 10.0))
        + np.diag(np.full(n - 1, 1.0), -1)
        + np.diag(np.full(n - 1, 1.0), 1)
    )
    b = np.random.RandomState(seed).rand(n)
    systems.append(("100-order SPD tridiagonal", A, b, np.linalg.solve(A, b)))

    n = 40
    index = np.arange(n, dtype=float)
    A = 1.0 / (index[:, None] + index[None, :] + 1.0)
    b = A @ np.ones(n)
    systems.append(("40-order Hilbert", A, b, np.ones(n)))

    return systems


def build_quadratic_fit_problem() -> tuple[Array, Array]:
    t = np.array([-1.0, -0.75, -0.5, 0.0, 0.25, 0.5, 0.75])
    y = np.array([1.00, 0.8125, 0.75, 1.00, 1.3125, 1.75, 2.3125])
    A = np.column_stack((t * t, t, np.ones_like(t)))
    return A, y


def build_housing_problem() -> tuple[Array, Array]:
    y = np.array(
        [
            25.9,
            29.5,
            27.9,
            25.9,
            29.9,
            29.9,
            30.9,
            28.9,
            84.9,
            82.9,
            35.9,
            31.5,
            31.0,
            30.9,
            30.0,
            28.9,
            36.9,
            41.9,
            40.5,
            43.9,
            37.5,
            37.9,
            44.5,
            37.9,
            38.9,
            36.9,
            45.8,
            41.0,
        ],
        dtype=float,
    )
    features = np.array(
        [
            [4.9176, 1.0, 3.4720, 0.9980, 1.0, 7, 4, 42, 3, 1, 0],
            [5.0208, 1.0, 3.5310, 1.5000, 2.0, 7, 4, 62, 1, 1, 0],
            [4.5429, 1.0, 2.2750, 1.1750, 1.0, 6, 3, 40, 2, 1, 0],
            [4.5573, 1.0, 4.0500, 1.2320, 1.0, 6, 3, 54, 4, 1, 0],
            [5.0597, 1.0, 4.4550, 1.1210, 1.0, 6, 3, 42, 3, 1, 0],
            [3.8910, 1.0, 4.4550, 0.9880, 1.0, 6, 3, 56, 2, 1, 0],
            [5.8980, 1.0, 5.8500, 1.2400, 1.0, 7, 3, 51, 2, 1, 1],
            [5.6039, 1.0, 9.5200, 1.5010, 0.0, 6, 3, 32, 1, 1, 0],
            [15.4202, 2.5, 9.8000, 3.4200, 2.0, 10, 5, 42, 2, 1, 1],
            [14.4598, 2.5, 12.8000, 3.0000, 2.0, 9, 5, 11, 4, 1, 1],
            [5.8282, 1.0, 6.4350, 1.2250, 2.0, 6, 3, 32, 1, 1, 0],
            [5.3003, 1.0, 4.9883, 1.5520, 1.0, 6, 3, 30, 1, 2, 0],
            [6.2712, 1.0, 5.5200, 0.9750, 1.0, 5, 2, 30, 1, 2, 0],
            [5.9592, 1.0, 6.6660, 1.1210, 2.0, 6, 3, 32, 2, 1, 0],
            [5.0500, 1.0, 5.0000, 1.0200, 0.0, 5, 2, 46, 4, 1, 1],
            [5.6039, 1.0, 9.5200, 1.5010, 0.0, 6, 3, 32, 1, 1, 0],
            [8.2464, 1.5, 5.1500, 1.6640, 2.0, 8, 4, 50, 4, 1, 0],
            [6.6969, 1.5, 6.0920, 1.4880, 1.5, 7, 3, 22, 1, 1, 1],
            [7.7841, 1.5, 7.1020, 1.3760, 1.0, 6, 3, 17, 2, 1, 0],
            [9.0384, 1.0, 7.8000, 1.5000, 1.5, 7, 3, 23, 3, 3, 0],
            [5.9894, 1.0, 5.5200, 1.2560, 2.0, 6, 3, 40, 4, 1, 1],
            [7.5422, 1.5, 4.0000, 1.6900, 1.0, 6, 3, 22, 1, 1, 0],
            [8.7951, 1.5, 9.8900, 1.8200, 2.0, 8, 4, 50, 1, 1, 1],
            [6.0931, 1.5, 6.7265, 1.6520, 1.0, 6, 3, 44, 4, 1, 0],
            [8.3607, 1.5, 9.1500, 1.7770, 2.0, 8, 4, 48, 1, 1, 1],
            [8.1400, 1.0, 8.0000, 1.5040, 2.0, 7, 3, 3, 1, 3, 0],
            [9.1416, 1.5, 7.3262, 1.8310, 1.5, 8, 4, 31, 4, 1, 0],
            [12.0000, 1.5, 5.0000, 1.2000, 2.0, 6, 3, 30, 3, 1, 1],
        ],
        dtype=float,
    )
    A = np.column_stack((np.ones(y.size), features))
    return A, y


@dataclass(frozen=True)
class MethodResult:
    system: str
    method: str
    residual_inf: float
    error_inf: float
    status: str


def _safe_method_result(
    system: str,
    method: str,
    solver: Callable[[Array, Array], Array],
    A: Array,
    b: Array,
    x_ref: Array,
) -> MethodResult:
    try:
        x = solver(A, b)
        if not np.all(np.isfinite(x)):
            raise FloatingPointError("nonfinite solution")
        residual = float(np.linalg.norm(b - A @ x, ord=np.inf))
        error = float(np.linalg.norm(x - x_ref, ord=np.inf))
        return MethodResult(system, method, residual, error, "ok")
    except Exception as exc:  # noqa: BLE001 - experiment table should record failures.
        return MethodResult(system, method, np.nan, np.nan, type(exc).__name__)


def first_chapter_comparison() -> list[MethodResult]:
    rows: list[MethodResult] = []
    for name, A, b, x_ref in build_first_chapter_systems():
        methods: list[tuple[str, Callable[[Array, Array], Array]]] = [
            ("Householder QR", qr_solve),
            ("Gauss no pivot", gauss_no_pivoting),
            ("Gauss partial pivot", gauss_partial_pivoting),
        ]
        if np.allclose(A, A.T):
            methods.extend(
                [
                    ("Cholesky", cholesky_solve),
                    ("LDLT", ldlt_solve),
                ]
            )
        for method_name, solver in methods:
            rows.append(_safe_method_result(name, method_name, solver, A, b, x_ref))
    return rows


def _format_float(value: float) -> str:
    if not np.isfinite(value):
        return "-"
    return f"{value:.6e}"


def _print_table(headers: Iterable[str], rows: Iterable[Iterable[str]]) -> None:
    rows = [list(row) for row in rows]
    headers = list(headers)
    widths = [
        max(len(str(item)) for item in column)
        for column in zip(headers, *rows, strict=False)
    ]
    print(" | ".join(header.ljust(width) for header, width in zip(headers, widths)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(str(item).ljust(width) for item, width in zip(row, widths)))


def main() -> None:
    print("Task 1: first-chapter linear systems")
    comparison_rows = first_chapter_comparison()
    _print_table(
        ["system", "method", "residual_inf", "error_inf", "status"],
        [
            [
                row.system,
                row.method,
                _format_float(row.residual_inf),
                _format_float(row.error_inf),
                row.status,
            ]
            for row in comparison_rows
        ],
    )

    print("\nTask 2: quadratic least squares y = a t^2 + b t + c")
    A_quad, y_quad = build_quadratic_fit_problem()
    coeff_quad = qr_least_squares(A_quad, y_quad)
    print(f"[a, b, c] = {coeff_quad}")
    print(f"residual_2 = {np.linalg.norm(A_quad @ coeff_quad - y_quad):.6e}")

    print("\nTask 3: housing least squares model")
    A_house, y_house = build_housing_problem()
    coeff_house = qr_least_squares(A_house, y_house)
    labels = ["x0"] + [f"a{i}" for i in range(1, 12)]
    for label, coeff in zip(labels, coeff_house):
        print(f"{label:>2} = {coeff: .10e}")
    residual = A_house @ coeff_house - y_house
    print(f"residual_2 = {np.linalg.norm(residual):.6e}")
    print(f"residual_inf = {np.linalg.norm(residual, ord=np.inf):.6e}")
    print(f"rank = {np.linalg.matrix_rank(A_house)}")
    print(f"cond_2 = {np.linalg.cond(A_house):.6e}")


if __name__ == "__main__":
    main()
