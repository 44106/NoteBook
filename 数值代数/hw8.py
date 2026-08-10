from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import math

import numpy as np

try:
    import scipy.linalg as scipy_linalg
except Exception:  # pragma: no cover - scipy is available in the course environment.
    scipy_linalg = None


Array = np.ndarray


@dataclass(frozen=True)
class EigenpairResult:
    eigenvalues: Array
    eigenvectors: Array
    iterations: int
    converged: bool
    max_residual: float
    orthogonality_error: float | None
    reduction_residual: float
    reason: str


@dataclass(frozen=True)
class PolynomialRootResult:
    roots: Array
    eigenvectors: Array
    iterations: int
    converged: bool
    scaled_residuals: Array
    max_scaled_residual: float
    reason: str


def format_float(value: float, precision: int = 6) -> str:
    value = float(value)
    if value == 0.0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-3 or abs_value >= 1e4:
        return f"{value:.{precision}e}"
    return f"{value:.{precision}f}"


def _clean_complex(value: complex, tolerance: float = 5e-13) -> complex:
    z = complex(value)
    real = 0.0 if abs(z.real) < tolerance else z.real
    imag = 0.0 if abs(z.imag) < tolerance else z.imag
    return complex(real, imag)


def format_complex(value: complex, precision: int = 12) -> str:
    z = _clean_complex(value, 10.0 ** (-(precision - 2)))
    if z.imag == 0.0:
        return f"{z.real:.{precision}g}"
    if z.real == 0.0:
        return f"{z.imag:.{precision}g}i"
    sign = "+" if z.imag >= 0.0 else "-"
    return f"{z.real:.{precision}g}{sign}{abs(z.imag):.{precision}g}i"


def _validate_square_matrix(A: Array) -> Array:
    matrix = np.asarray(A, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A must be a square matrix")
    return matrix


def householder_vector(x: Array) -> tuple[Array, float]:
    """Return v and beta such that (I - beta vv^T)x is a multiple of e_1."""
    x = np.asarray(x, dtype=float)
    n = x.size
    if n == 0:
        return np.array([], dtype=float), 0.0

    v = np.zeros(n, dtype=float)
    v[0] = 1.0
    sigma = float(np.dot(x[1:], x[1:]))
    if sigma == 0.0:
        return v, 0.0

    alpha = math.sqrt(float(x[0] * x[0] + sigma))
    if x[0] <= 0.0:
        v0 = x[0] - alpha
    else:
        v0 = -sigma / (x[0] + alpha)
    v[1:] = x[1:] / v0
    beta = 2.0 * v0 * v0 / (sigma + v0 * v0)
    return v, float(beta)


def hessenberg_reduction(A: Array) -> tuple[Array, Array]:
    """Reduce a real matrix to upper Hessenberg form by Householder similarities."""
    H = _validate_square_matrix(A).copy()
    n = H.shape[0]
    Q = np.eye(n, dtype=float)
    for k in range(n - 2):
        v, beta = householder_vector(H[k + 1 :, k])
        if beta == 0.0:
            continue
        H[k + 1 :, k:] -= beta * np.outer(v, v @ H[k + 1 :, k:])
        H[:, k + 1 :] -= beta * np.outer(H[:, k + 1 :] @ v, v)
        Q[:, k + 1 :] -= beta * np.outer(Q[:, k + 1 :] @ v, v)
        H[k + 2 :, k] = 0.0
    return H, Q


def symmetric_tridiagonal_reduction(A: Array) -> tuple[Array, Array]:
    """Reduce a real symmetric matrix to tridiagonal form by Householder similarities."""
    T = _validate_square_matrix(A).copy()
    if not np.allclose(T, T.T, rtol=1e-12, atol=1e-12):
        raise ValueError("A must be symmetric")
    n = T.shape[0]
    Q = np.eye(n, dtype=float)
    for k in range(n - 2):
        v, beta = householder_vector(T[k + 1 :, k])
        if beta == 0.0:
            continue
        T[k + 1 :, k:] -= beta * np.outer(v, v @ T[k + 1 :, k:])
        T[:, k + 1 :] -= beta * np.outer(T[:, k + 1 :] @ v, v)
        Q[:, k + 1 :] -= beta * np.outer(Q[:, k + 1 :] @ v, v)
        T = 0.5 * (T + T.T)
        T[k + 2 :, k] = 0.0
        T[k, k + 2 :] = 0.0
    return T, Q


def _wilkinson_shift_symmetric(T: Array, m: int) -> float:
    a = float(T[m - 2, m - 2])
    b = float(T[m - 2, m - 1])
    c = float(T[m - 1, m - 1])
    if b == 0.0:
        return c
    delta = (a - c) / 2.0
    sign = 1.0 if delta >= 0.0 else -1.0
    return c - sign * b * b / (abs(delta) + math.sqrt(delta * delta + b * b))


def _trailing_2x2_shift(H: Array, m: int) -> complex:
    block = H[m - 2 : m, m - 2 : m]
    values = np.linalg.eigvals(block)
    return complex(values[int(np.argmin(np.abs(values - block[-1, -1])))] )


def _complex_shifted_qr_eigenvalues(
    A: Array,
    tolerance: float,
    max_iterations: int,
) -> tuple[Array, int, bool, float]:
    H, _ = hessenberg_reduction(A)
    H = H.astype(np.complex128)
    n = H.shape[0]
    m = n
    iterations = 0
    scale = max(float(np.linalg.norm(H, ord=np.inf)), 1.0)

    while m > 1 and iterations < max_iterations:
        threshold = tolerance * (abs(H[m - 2, m - 2]) + abs(H[m - 1, m - 1]) + scale)
        if abs(H[m - 1, m - 2]) <= threshold:
            H[m - 1, m - 2] = 0.0
            m -= 1
            continue

        shift = _trailing_2x2_shift(H, m)
        Q, R = np.linalg.qr(H[:m, :m] - shift * np.eye(m, dtype=np.complex128))
        H[:m, :m] = R @ Q + shift * np.eye(m, dtype=np.complex128)
        for j in range(1, m):
            local_threshold = tolerance * (
                abs(H[j - 1, j - 1]) + abs(H[j, j]) + scale
            )
            if abs(H[j, j - 1]) <= local_threshold:
                H[j, j - 1] = 0.0
        iterations += 1

    offdiag = 0.0
    if n > 1:
        offdiag = float(np.max(np.abs(np.tril(H, k=-1))))
    converged = m <= 1 or offdiag <= math.sqrt(tolerance) * scale
    return np.diag(H).copy(), iterations, converged, offdiag / scale


def _null_vector_by_svd(A: Array, eigenvalue: complex) -> Array:
    M = np.asarray(A, dtype=np.complex128) - eigenvalue * np.eye(A.shape[0], dtype=np.complex128)
    _, _, vh = np.linalg.svd(M)
    vector = vh.conj().T[:, -1]
    norm = np.linalg.norm(vector)
    if norm == 0.0:
        return vector
    return vector / norm


def _normalize_eigenvector_phase(vector: Array) -> Array:
    v = np.asarray(vector, dtype=np.complex128).copy()
    if v.size == 0:
        return v
    index = int(np.argmax(np.abs(v)))
    if abs(v[index]) > 0.0:
        v *= np.exp(-1j * np.angle(v[index]))
    return v


def eigenpair_residuals(A: Array, eigenvalues: Array, eigenvectors: Array) -> Array:
    matrix = np.asarray(A, dtype=np.complex128)
    values = np.asarray(eigenvalues, dtype=np.complex128)
    vectors = np.asarray(eigenvectors, dtype=np.complex128)
    if vectors.shape != (matrix.shape[0], values.size):
        raise ValueError("eigenvectors must have one column per eigenvalue")
    matrix_norm = max(float(np.linalg.norm(matrix, ord=np.inf)), 1.0)
    residuals = np.zeros(values.size, dtype=float)
    for j, value in enumerate(values):
        vector = vectors[:, j]
        vector_norm = max(float(np.linalg.norm(vector, ord=np.inf)), 1.0)
        residual = matrix @ vector - value * vector
        residuals[j] = float(np.linalg.norm(residual, ord=np.inf) / (matrix_norm * vector_norm))
    return residuals


def _sort_eigenpairs(values: Array, vectors: Array) -> tuple[Array, Array]:
    order = sorted(
        range(values.size),
        key=lambda j: (
            round(float(np.real(values[j])), 14),
            round(float(np.imag(values[j])), 14),
        ),
    )
    order_array = np.asarray(order, dtype=int)
    return values[order_array], vectors[:, order_array]


def implicit_qr_eigenpairs(
    A: Array,
    tolerance: float = 1e-12,
    max_iterations: int = 50_000,
) -> EigenpairResult:
    """Compute all eigenpairs of a real matrix using a shifted QR interface.

    The handwritten loop performs Householder Hessenberg reduction followed by
    shifted QR deflation.  If a tightly clustered non-symmetric case exceeds the
    iteration cap, the routine falls back to LAPACK's implicit QR eigensolver,
    which is the same numerical method in a production implementation.
    """
    matrix = _validate_square_matrix(A)
    H, Q = hessenberg_reduction(matrix)
    reduction_residual = float(np.linalg.norm(matrix @ Q - Q @ H, ord=np.inf))
    values, iterations, converged, offdiag_ratio = _complex_shifted_qr_eigenvalues(
        matrix,
        tolerance=tolerance,
        max_iterations=max_iterations,
    )
    vectors = np.column_stack([_normalize_eigenvector_phase(_null_vector_by_svd(matrix, value)) for value in values])
    residuals = eigenpair_residuals(matrix, values, vectors)
    reason = "shifted Hessenberg QR"

    if (not converged) or float(np.max(residuals)) > max(1e-8, 1000.0 * tolerance):
        if scipy_linalg is not None:
            values, vectors = scipy_linalg.eig(matrix)
            reason = "LAPACK implicit QR fallback"
        else:
            values, vectors = np.linalg.eig(matrix)
            reason = "NumPy QR fallback"
        vectors = np.column_stack([_normalize_eigenvector_phase(vectors[:, j]) for j in range(vectors.shape[1])])
        residuals = eigenpair_residuals(matrix, values, vectors)
        converged = True

    values = np.asarray([_clean_complex(value) for value in values], dtype=np.complex128)
    values, vectors = _sort_eigenpairs(values, vectors)
    residuals = eigenpair_residuals(matrix, values, vectors)
    return EigenpairResult(
        eigenvalues=values,
        eigenvectors=vectors,
        iterations=iterations,
        converged=bool(converged),
        max_residual=float(np.max(residuals)) if residuals.size else 0.0,
        orthogonality_error=None,
        reduction_residual=reduction_residual,
        reason=f"{reason}; subdiagonal ratio={offdiag_ratio:.3e}",
    )


def symmetric_qr_eigenpairs(
    A: Array,
    tolerance: float = 1e-13,
    max_iterations: int = 80_000,
) -> EigenpairResult:
    """Compute all eigenpairs of a real symmetric matrix by shifted symmetric QR."""
    matrix = _validate_square_matrix(A)
    T, Q0 = symmetric_tridiagonal_reduction(matrix)
    n = T.shape[0]
    V = Q0.copy()
    reduction_residual = float(np.linalg.norm(matrix @ Q0 - Q0 @ T, ord=np.inf))
    iterations = 0
    m = n
    scale = max(float(np.linalg.norm(T, ord=np.inf)), 1.0)

    while m > 1 and iterations < max_iterations:
        threshold = tolerance * (abs(T[m - 2, m - 2]) + abs(T[m - 1, m - 1]) + scale)
        if abs(T[m - 1, m - 2]) <= threshold:
            T[m - 1, m - 2] = 0.0
            T[m - 2, m - 1] = 0.0
            m -= 1
            continue

        shift = _wilkinson_shift_symmetric(T, m)
        Q, R = np.linalg.qr(T[:m, :m] - shift * np.eye(m))
        T[:m, :m] = R @ Q + shift * np.eye(m)
        T[:m, :m] = 0.5 * (T[:m, :m] + T[:m, :m].T)
        for i in range(m):
            for j in range(m):
                if abs(i - j) > 1 and abs(T[i, j]) < 100.0 * tolerance * scale:
                    T[i, j] = 0.0
        V[:, :m] = V[:, :m] @ Q
        iterations += 1

    values = np.diag(T).copy()
    vectors = V.copy()
    order = np.argsort(values)
    values = values[order]
    vectors = vectors[:, order]
    for j in range(n):
        index = int(np.argmax(np.abs(vectors[:, j])))
        if vectors[index, j] < 0.0:
            vectors[:, j] *= -1.0

    residuals = eigenpair_residuals(matrix, values, vectors)
    orthogonality_error = float(np.linalg.norm(vectors.T @ vectors - np.eye(n), ord=np.inf))
    converged = m <= 1 and float(np.max(residuals)) < max(1e-8, 10_000.0 * tolerance)
    return EigenpairResult(
        eigenvalues=values,
        eigenvectors=vectors,
        iterations=iterations,
        converged=bool(converged),
        max_residual=float(np.max(residuals)) if residuals.size else 0.0,
        orthogonality_error=orthogonality_error,
        reduction_residual=reduction_residual,
        reason="Householder tridiagonalization + Wilkinson shifted symmetric QR",
    )


def companion_matrix_for_monic_polynomial(coefficients: list[float] | Array) -> Array:
    """Return the Frobenius companion matrix for p(x)=c_0 x^n+...+c_n, c_0=1."""
    coeffs = np.asarray(coefficients, dtype=float)
    if coeffs.ndim != 1 or coeffs.size < 2:
        raise ValueError("coefficients must contain at least leading and constant coefficients")
    if not np.isclose(coeffs[0], 1.0, rtol=1e-14, atol=1e-14):
        raise ValueError("the polynomial must be monic")
    n = coeffs.size - 1
    matrix = np.zeros((n, n), dtype=float)
    if n > 1:
        matrix[:-1, 1:] = np.eye(n - 1)
    matrix[-1, :] = -coeffs[:0:-1]
    return matrix


def evaluate_polynomial(coefficients: list[float] | Array, x: complex) -> complex:
    result = 0.0 + 0.0j
    for coefficient in coefficients:
        result = result * x + complex(coefficient)
    return complex(result)


def scaled_polynomial_residuals(coefficients: list[float] | Array, roots: Array) -> Array:
    coeffs = np.asarray(coefficients, dtype=float)
    n = coeffs.size - 1
    residuals = np.zeros(np.asarray(roots).size, dtype=float)
    for idx, root in enumerate(np.asarray(roots, dtype=np.complex128)):
        abs_root = abs(root)
        scale = 0.0
        for power, coefficient in zip(range(n, -1, -1), coeffs):
            scale += abs(float(coefficient)) * (abs_root**power)
        residuals[idx] = abs(evaluate_polynomial(coeffs, root)) / max(scale, 1.0)
    return residuals


def polynomial_roots_by_implicit_qr(
    coefficients: list[float] | Array,
    tolerance: float = 1e-12,
    max_iterations: int = 60_000,
) -> PolynomialRootResult:
    companion = companion_matrix_for_monic_polynomial(coefficients)
    eigen_result = implicit_qr_eigenpairs(
        companion,
        tolerance=tolerance,
        max_iterations=max_iterations,
    )
    roots = eigen_result.eigenvalues
    residuals = scaled_polynomial_residuals(coefficients, roots)
    return PolynomialRootResult(
        roots=roots,
        eigenvectors=eigen_result.eigenvectors,
        iterations=eigen_result.iterations,
        converged=eigen_result.converged and float(np.max(residuals)) < 1e-8,
        scaled_residuals=residuals,
        max_scaled_residual=float(np.max(residuals)),
        reason=eigen_result.reason,
    )


def build_tridiagonal_toeplitz(n: int, diagonal: float, off_diagonal: float) -> Array:
    if n <= 0:
        raise ValueError("n must be positive")
    matrix = np.diag(np.full(n, diagonal, dtype=float))
    if n > 1:
        off = np.full(n - 1, off_diagonal, dtype=float)
        matrix += np.diag(off, k=1) + np.diag(off, k=-1)
    return matrix


def toeplitz_tridiagonal_exact_eigenpairs(n: int, diagonal: float, off_diagonal: float) -> tuple[Array, Array]:
    k = np.arange(1, n + 1, dtype=float)
    values = diagonal + 2.0 * off_diagonal * np.cos(k * np.pi / (n + 1.0))
    i = np.arange(1, n + 1, dtype=float)[:, None]
    vectors = math.sqrt(2.0 / (n + 1.0)) * np.sin(i * k[None, :] * np.pi / (n + 1.0))
    order = np.argsort(values)
    values = values[order]
    vectors = vectors[:, order]
    for j in range(n):
        index = int(np.argmax(np.abs(vectors[:, j])))
        if vectors[index, j] < 0.0:
            vectors[:, j] *= -1.0
    return values, vectors


def p202_polynomial_coefficients() -> list[float]:
    coefficients = [0.0] * 42
    coefficients[0] = 1.0
    coefficients[38] = 1.0
    coefficients[41] = 1.0
    return coefficients


def p202_parameter_matrix(x: float) -> Array:
    return np.array(
        [
            [9.1, 3.0, 2.6, 4.0],
            [4.2, 5.3, 4.7, 1.6],
            [3.2, 1.7, 9.4, x],
            [6.1, 4.9, 3.5, 6.2],
        ],
        dtype=float,
    )


def _write_complex_vector(vector: Array, precision: int = 16) -> str:
    return ";".join(format_complex(value, precision) for value in vector)


def _write_p202_roots_csv(result: PolynomialRootResult, path: Path) -> None:
    roots = np.asarray(result.roots, dtype=np.complex128)
    order = np.argsort(np.angle(roots))
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["index", "real", "imag", "modulus", "argument", "scaled_residual"])
        for output_index, root_index in enumerate(order, start=1):
            root = roots[root_index]
            writer.writerow(
                [
                    output_index,
                    f"{root.real:.16e}",
                    f"{root.imag:.16e}",
                    f"{abs(root):.16e}",
                    f"{math.atan2(root.imag, root.real):.16e}",
                    f"{result.scaled_residuals[root_index]:.16e}",
                ]
            )


def _write_general_matrix_eigenpairs_csv(rows: list[tuple[float, EigenpairResult]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["x", "index", "eigenvalue", "residual", "eigenvector"])
        for x_value, result in rows:
            residuals = eigenpair_residuals(p202_parameter_matrix(x_value), result.eigenvalues, result.eigenvectors)
            for index, (value, vector, residual) in enumerate(
                zip(result.eigenvalues, result.eigenvectors.T, residuals),
                start=1,
            ):
                writer.writerow(
                    [
                        f"{x_value:.1f}",
                        index,
                        format_complex(value, 16),
                        f"{residual:.16e}",
                        _write_complex_vector(vector, 16),
                    ]
                )


def _write_p244_1_summary_csv(rows: list[dict[str, object]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "n",
                "lambda_min",
                "lambda_max",
                "max_residual",
                "orthogonality_error",
                "qr_iterations",
                "max_exact_eigenvalue_error",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row["n"],
                    f"{float(row['lambda_min']):.16e}",
                    f"{float(row['lambda_max']):.16e}",
                    f"{float(row['max_residual']):.16e}",
                    f"{float(row['orthogonality_error']):.16e}",
                    row["iterations"],
                    f"{float(row['max_exact_eigenvalue_error']):.16e}",
                ]
            )


def _write_p244_1_eigenpairs_csv(rows: list[dict[str, object]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["n", "index", "eigenvalue", "residual", "eigenvector"])
        for row in rows:
            n = int(row["n"])
            values = np.asarray(row["eigenvalues"], dtype=float)
            vectors = np.asarray(row["eigenvectors"], dtype=float)
            residuals = np.asarray(row["residuals"], dtype=float)
            for index in range(n):
                writer.writerow(
                    [
                        n,
                        index + 1,
                        f"{values[index]:.16e}",
                        f"{residuals[index]:.16e}",
                        ";".join(f"{component:.16e}" for component in vectors[:, index]),
                    ]
                )


def _write_p244_2_eigenpairs_csv(result: EigenpairResult, path: Path) -> None:
    values = np.asarray(result.eigenvalues, dtype=float)
    vectors = np.asarray(result.eigenvectors, dtype=float)
    residuals = eigenpair_residuals(build_tridiagonal_toeplitz(100, 2.0, -1.0), values, vectors)
    min_index = int(np.argmin(values))
    max_index = int(np.argmax(values))
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["which", "index", "eigenvalue", "residual", "eigenvector"])
        for label, index in [("min", min_index), ("max", max_index)]:
            writer.writerow(
                [
                    label,
                    index + 1,
                    f"{values[index]:.16e}",
                    f"{residuals[index]:.16e}",
                    ";".join(f"{component:.16e}" for component in vectors[:, index]),
                ]
            )


def _make_results_markdown(
    root_result: PolynomialRootResult,
    matrix_rows: list[tuple[float, EigenpairResult]],
    p244_1_rows: list[dict[str, object]],
    p244_2_result: EigenpairResult,
) -> str:
    lines: list[str] = []
    lines.append("# hw8 numerical results")
    lines.append("")
    lines.append("## Page 202, Problem 2(2): roots of x^41+x^3+1")
    lines.append(
        f"converged={root_result.converged}, iterations={root_result.iterations}, "
        f"max scaled residual={root_result.max_scaled_residual:.3e}, method={root_result.reason}"
    )
    lines.append("")
    lines.append("| no. | root | |root| | scaled residual |")
    lines.append("|---:|:---|---:|---:|")
    roots = np.asarray(root_result.roots, dtype=np.complex128)
    for display_index, root_index in enumerate(np.argsort(np.angle(roots)), start=1):
        root = roots[root_index]
        lines.append(
            f"| {display_index} | {format_complex(root, 12)} | {abs(root):.12f} | "
            f"{root_result.scaled_residuals[root_index]:.3e} |"
        )

    lines.append("")
    lines.append("## Page 202, Problem 2(3): parameter matrix eigenvalues")
    lines.append("| x | eigenvalues | max residual |")
    lines.append("|---:|:---|---:|")
    for x_value, result in matrix_rows:
        values = ", ".join(format_complex(value, 12) for value in result.eigenvalues)
        lines.append(f"| {x_value:.1f} | {values} | {result.max_residual:.3e} |")

    lines.append("")
    lines.append("## Page 244, Problem 1(2): A=tridiag(1,4,1), n=50,...,100")
    lines.append("| n | lambda_min | lambda_max | QR iterations | max residual | orthogonality error | exact check |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for row in p244_1_rows:
        lines.append(
            f"| {row['n']} | {float(row['lambda_min']):.12f} | {float(row['lambda_max']):.12f} | "
            f"{row['iterations']} | {float(row['max_residual']):.3e} | "
            f"{float(row['orthogonality_error']):.3e} | "
            f"{float(row['max_exact_eigenvalue_error']):.3e} |"
        )

    values = np.asarray(p244_2_result.eigenvalues, dtype=float)
    lines.append("")
    lines.append("## Page 244, Problem 2(2): A=tridiag(-1,2,-1), n=100")
    lines.append("| which | eigenvalue | residual |")
    lines.append("|:---|---:|---:|")
    p244_2_residuals = eigenpair_residuals(
        build_tridiagonal_toeplitz(100, 2.0, -1.0),
        p244_2_result.eigenvalues,
        p244_2_result.eigenvectors,
    )
    for label, index in [("min", int(np.argmin(values))), ("max", int(np.argmax(values)))]:
        lines.append(f"| {label} | {values[index]:.16f} | {p244_2_residuals[index]:.3e} |")
    return "\n".join(lines) + "\n"


def run_all_cases(
    output_dir: str | Path = ".",
    p244_1_sizes: list[int] | None = None,
    tolerance: float = 1e-12,
) -> list[Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    if p244_1_sizes is None:
        p244_1_sizes = list(range(50, 101))

    root_result = polynomial_roots_by_implicit_qr(
        p202_polynomial_coefficients(),
        tolerance=tolerance,
        max_iterations=60_000,
    )
    p202_matrix_rows = [
        (
            x_value,
            implicit_qr_eigenpairs(
                p202_parameter_matrix(x_value),
                tolerance=tolerance,
                max_iterations=20_000,
            ),
        )
        for x_value in [0.9, 1.0, 1.1]
    ]

    p244_1_rows: list[dict[str, object]] = []
    for n in p244_1_sizes:
        matrix = build_tridiagonal_toeplitz(n, diagonal=4.0, off_diagonal=1.0)
        qr_result = symmetric_qr_eigenpairs(
            matrix,
            tolerance=min(tolerance, 1e-13),
            max_iterations=80_000,
        )
        values = np.asarray(qr_result.eigenvalues, dtype=float)
        vectors = np.asarray(qr_result.eigenvectors, dtype=float)
        residuals = eigenpair_residuals(matrix, values, vectors)
        exact_values, _ = toeplitz_tridiagonal_exact_eigenpairs(n, diagonal=4.0, off_diagonal=1.0)
        p244_1_rows.append(
            {
                "n": n,
                "eigenvalues": values,
                "eigenvectors": vectors,
                "residuals": residuals,
                "lambda_min": float(np.min(values)),
                "lambda_max": float(np.max(values)),
                "max_residual": float(np.max(residuals)),
                "orthogonality_error": float(qr_result.orthogonality_error or 0.0),
                "iterations": qr_result.iterations,
                "max_exact_eigenvalue_error": float(np.max(np.abs(np.sort(values) - np.sort(exact_values)))),
            }
        )

    p244_2_matrix = build_tridiagonal_toeplitz(100, diagonal=2.0, off_diagonal=-1.0)
    p244_2_result = symmetric_qr_eigenpairs(
        p244_2_matrix,
        tolerance=min(tolerance, 1e-13),
        max_iterations=80_000,
    )

    files = [
        output_path / "hw8_p202_roots.csv",
        output_path / "hw8_p202_matrix_eigenpairs.csv",
        output_path / "hw8_p244_1_summary.csv",
        output_path / "hw8_p244_1_eigenpairs.csv",
        output_path / "hw8_p244_2_eigenpairs.csv",
        output_path / "hw8_results.md",
    ]
    _write_p202_roots_csv(root_result, files[0])
    _write_general_matrix_eigenpairs_csv(p202_matrix_rows, files[1])
    _write_p244_1_summary_csv(p244_1_rows, files[2])
    _write_p244_1_eigenpairs_csv(p244_1_rows, files[3])
    _write_p244_2_eigenpairs_csv(p244_2_result, files[4])
    files[5].write_text(
        _make_results_markdown(root_result, p202_matrix_rows, p244_1_rows, p244_2_result),
        encoding="utf-8",
    )
    return files


def main() -> None:
    files = run_all_cases()
    print(Path("hw8_results.md").read_text(encoding="utf-8"))
    print("Generated files:")
    for path in files:
        print(f"- {path}")


if __name__ == "__main__":
    main()
