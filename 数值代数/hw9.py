from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import math

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class JacobiResult:
    eigenvalues: Array
    eigenvectors: Array
    diagonalized_matrix: Array
    rotations: int
    sweeps: float
    converged: bool
    off_diagonal_norm: float
    max_residual: float
    orthogonality_error: float
    max_exact_eigenvalue_error: float | None = None
    max_exact_vector_angle_error: float | None = None


def _validate_symmetric_matrix(A: Array) -> Array:
    matrix = np.asarray(A, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A must be a square matrix")
    if not np.allclose(matrix, matrix.T, rtol=1e-12, atol=1e-12):
        raise ValueError("A must be symmetric")
    return matrix


def build_tridiagonal_toeplitz(n: int, diagonal: float, off_diagonal: float) -> Array:
    if n <= 0:
        raise ValueError("n must be positive")
    matrix = np.diag(np.full(n, diagonal, dtype=float))
    if n > 1:
        off = np.full(n - 1, off_diagonal, dtype=float)
        matrix += np.diag(off, k=1) + np.diag(off, k=-1)
    return matrix


def toeplitz_tridiagonal_exact_eigenpairs(n: int, diagonal: float, off_diagonal: float) -> tuple[Array, Array]:
    if n <= 0:
        raise ValueError("n must be positive")
    k = np.arange(1, n + 1, dtype=float)
    values = diagonal + 2.0 * off_diagonal * np.cos(k * np.pi / (n + 1.0))
    i = np.arange(1, n + 1, dtype=float)[:, None]
    vectors = math.sqrt(2.0 / (n + 1.0)) * np.sin(i * k[None, :] * np.pi / (n + 1.0))
    order = np.argsort(values)
    values = values[order]
    vectors = vectors[:, order]
    return _normalize_vector_signs(values, vectors)


def off_diagonal_norm(A: Array) -> float:
    matrix = np.asarray(A, dtype=float)
    return float(np.linalg.norm(matrix - np.diag(np.diag(matrix)), ord="fro"))


def _largest_off_diagonal_entry(A: Array) -> tuple[int, int, float]:
    n = A.shape[0]
    if n < 2:
        return 0, 0, 0.0
    upper = np.triu(np.abs(A), k=1)
    flat_index = int(np.argmax(upper))
    p, q = divmod(flat_index, n)
    return p, q, float(A[p, q])


def _rotation_parameters(app: float, apq: float, aqq: float) -> tuple[float, float, float]:
    if apq == 0.0:
        return 1.0, 0.0, 0.0
    tau = (aqq - app) / (2.0 * apq)
    if tau == 0.0:
        t = 1.0
    else:
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
    c = 1.0 / math.sqrt(1.0 + t * t)
    s = t * c
    return c, s, t


def _apply_jacobi_rotation(A: Array, V: Array, p: int, q: int) -> None:
    app = float(A[p, p])
    apq = float(A[p, q])
    aqq = float(A[q, q])
    c, s, t = _rotation_parameters(app, apq, aqq)
    if s == 0.0:
        A[p, q] = 0.0
        A[q, p] = 0.0
        return

    n = A.shape[0]
    for i in range(n):
        if i == p or i == q:
            continue
        aip = float(A[i, p])
        aiq = float(A[i, q])
        new_ip = c * aip - s * aiq
        new_iq = s * aip + c * aiq
        A[i, p] = new_ip
        A[p, i] = new_ip
        A[i, q] = new_iq
        A[q, i] = new_iq

    A[p, p] = app - t * apq
    A[q, q] = aqq + t * apq
    A[p, q] = 0.0
    A[q, p] = 0.0

    vp = V[:, p].copy()
    vq = V[:, q].copy()
    V[:, p] = c * vp - s * vq
    V[:, q] = s * vp + c * vq


def _normalize_vector_signs(values: Array, vectors: Array) -> tuple[Array, Array]:
    values = np.asarray(values, dtype=float).copy()
    vectors = np.asarray(vectors, dtype=float).copy()
    order = np.argsort(values)
    values = values[order]
    vectors = vectors[:, order]
    for j in range(vectors.shape[1]):
        index = int(np.argmax(np.abs(vectors[:, j])))
        if vectors[index, j] < 0.0:
            vectors[:, j] *= -1.0
    return values, vectors


def eigenpair_residuals(A: Array, eigenvalues: Array, eigenvectors: Array) -> Array:
    matrix = np.asarray(A, dtype=float)
    values = np.asarray(eigenvalues, dtype=float)
    vectors = np.asarray(eigenvectors, dtype=float)
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


def jacobi_eigenpairs(
    A: Array,
    tolerance: float = 1e-12,
    max_sweeps: int = 300,
) -> JacobiResult:
    """Compute all eigenpairs of a real symmetric matrix by the classic Jacobi method.

    Each rotation plane is selected by the textbook rule
    |a[p,q]| = max_{i<j} |a[i,j]|.  The rotation uses
    tau=(a[q,q]-a[p,p])/(2a[p,q]) and the smaller root
    t=sign(tau)/(|tau|+sqrt(1+tau^2)), followed by c=1/sqrt(1+t^2), s=tc.
    """
    matrix = _validate_symmetric_matrix(A)
    n = matrix.shape[0]
    diagonalized = matrix.copy()
    eigenvectors = np.eye(n, dtype=float)
    if n <= 1:
        values, vectors = _normalize_vector_signs(np.diag(diagonalized), eigenvectors)
        return JacobiResult(values, vectors, diagonalized, 0, 0.0, True, 0.0, 0.0, 0.0)

    initial_norm = max(off_diagonal_norm(diagonalized), 1.0)
    threshold = tolerance * initial_norm
    max_rotations = max_sweeps * n * (n - 1) // 2
    rotations = 0

    while rotations < max_rotations:
        current_off = off_diagonal_norm(diagonalized)
        if current_off <= threshold:
            break
        p, q, apq = _largest_off_diagonal_entry(diagonalized)
        if abs(apq) <= threshold / math.sqrt(max(n * (n - 1), 1)):
            break
        _apply_jacobi_rotation(diagonalized, eigenvectors, p, q)
        rotations += 1

    final_off = off_diagonal_norm(diagonalized)
    values, vectors = _normalize_vector_signs(np.diag(diagonalized), eigenvectors)
    residuals = eigenpair_residuals(matrix, values, vectors)
    orthogonality_error = float(np.linalg.norm(vectors.T @ vectors - np.eye(n), ord=np.inf))
    converged = final_off <= max(threshold, 10.0 * np.finfo(float).eps * max(float(np.linalg.norm(matrix, ord="fro")), 1.0))
    sweeps = rotations / (n * (n - 1) / 2.0)
    return JacobiResult(
        eigenvalues=values,
        eigenvectors=vectors,
        diagonalized_matrix=diagonalized,
        rotations=rotations,
        sweeps=sweeps,
        converged=bool(converged),
        off_diagonal_norm=final_off,
        max_residual=float(np.max(residuals)) if residuals.size else 0.0,
        orthogonality_error=orthogonality_error,
    )


def _vector_angle_errors(vectors: Array, exact_vectors: Array) -> Array:
    alignments = np.abs(np.sum(np.asarray(vectors) * np.asarray(exact_vectors), axis=0))
    return 1.0 - np.clip(alignments, 0.0, 1.0)


def _write_summary_csv(rows: list[dict[str, object]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "n",
                "lambda_min",
                "lambda_max",
                "rotations",
                "sweeps",
                "off_diagonal_norm",
                "max_residual",
                "orthogonality_error",
                "max_exact_eigenvalue_error",
                "max_exact_vector_angle_error",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row["n"],
                    f"{float(row['lambda_min']):.16e}",
                    f"{float(row['lambda_max']):.16e}",
                    row["rotations"],
                    f"{float(row['sweeps']):.8f}",
                    f"{float(row['off_diagonal_norm']):.16e}",
                    f"{float(row['max_residual']):.16e}",
                    f"{float(row['orthogonality_error']):.16e}",
                    f"{float(row['max_exact_eigenvalue_error']):.16e}",
                    f"{float(row['max_exact_vector_angle_error']):.16e}",
                ]
            )


def _write_eigenpairs_csv(rows: list[dict[str, object]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["n", "index", "eigenvalue", "residual", "exact_eigenvalue", "eigenvector"])
        for row in rows:
            n = int(row["n"])
            values = np.asarray(row["eigenvalues"], dtype=float)
            exact_values = np.asarray(row["exact_eigenvalues"], dtype=float)
            vectors = np.asarray(row["eigenvectors"], dtype=float)
            residuals = np.asarray(row["residuals"], dtype=float)
            for index in range(n):
                writer.writerow(
                    [
                        n,
                        index + 1,
                        f"{values[index]:.16e}",
                        f"{residuals[index]:.16e}",
                        f"{exact_values[index]:.16e}",
                        ";".join(f"{component:.16e}" for component in vectors[:, index]),
                    ]
                )


def _make_results_markdown(rows: list[dict[str, object]]) -> str:
    lines: list[str] = []
    lines.append("# hw9 numerical results")
    lines.append("")
    lines.append("## Page 244, Problem 1: classic Jacobi method for A=tridiag(1,4,1), n=50,...,100")
    lines.append("")
    lines.append("| n | lambda_min | lambda_max | rotations | sweeps | offdiag Frobenius | max residual | orthogonality | exact eig err |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| {row['n']} | {float(row['lambda_min']):.12f} | {float(row['lambda_max']):.12f} | "
            f"{row['rotations']} | {float(row['sweeps']):.2f} | {float(row['off_diagonal_norm']):.3e} | "
            f"{float(row['max_residual']):.3e} | {float(row['orthogonality_error']):.3e} | "
            f"{float(row['max_exact_eigenvalue_error']):.3e} |"
        )
    return "\n".join(lines) + "\n"


def run_all_cases(
    output_dir: str | Path = ".",
    sizes: list[int] | None = None,
    tolerance: float = 1e-12,
) -> list[Path]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    if sizes is None:
        sizes = list(range(50, 101))

    rows: list[dict[str, object]] = []
    for n in sizes:
        matrix = build_tridiagonal_toeplitz(n, diagonal=4.0, off_diagonal=1.0)
        result = jacobi_eigenpairs(matrix, tolerance=tolerance, max_sweeps=300)
        exact_values, exact_vectors = toeplitz_tridiagonal_exact_eigenpairs(n, diagonal=4.0, off_diagonal=1.0)
        residuals = eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors)
        value_error = float(np.max(np.abs(result.eigenvalues - exact_values)))
        angle_error = float(np.max(_vector_angle_errors(result.eigenvectors, exact_vectors)))
        rows.append(
            {
                "n": n,
                "eigenvalues": result.eigenvalues,
                "eigenvectors": result.eigenvectors,
                "exact_eigenvalues": exact_values,
                "residuals": residuals,
                "lambda_min": float(result.eigenvalues[0]),
                "lambda_max": float(result.eigenvalues[-1]),
                "rotations": result.rotations,
                "sweeps": result.sweeps,
                "off_diagonal_norm": result.off_diagonal_norm,
                "max_residual": float(np.max(residuals)),
                "orthogonality_error": result.orthogonality_error,
                "max_exact_eigenvalue_error": value_error,
                "max_exact_vector_angle_error": angle_error,
            }
        )

    files = [
        output_path / "hw9_summary.csv",
        output_path / "hw9_eigenpairs.csv",
        output_path / "hw9_results.md",
    ]
    _write_summary_csv(rows, files[0])
    _write_eigenpairs_csv(rows, files[1])
    files[2].write_text(_make_results_markdown(rows), encoding="utf-8")
    return files


if __name__ == "__main__":
    for output in run_all_cases():
        print(output)
