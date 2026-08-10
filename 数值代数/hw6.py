from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class IterationConfig:
    tolerance: float = 1e-10
    max_iterations: int = 10000


@dataclass(frozen=True)
class IterationResult:
    method: str
    x: Array
    iterations: int
    converged: bool
    residual_norm: float
    relative_residual_norm: float
    last_step_norm: float


def _as_system(A: Array, b: Array) -> tuple[Array, Array]:
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be a square matrix")
    if b.ndim != 1 or b.size != A.shape[0]:
        raise ValueError("b must be a vector with length matching A")
    return A, b


def _initial_guess(b: Array, x0: Array | None) -> Array:
    if x0 is None:
        return np.zeros_like(b, dtype=float)
    x = np.asarray(x0, dtype=float)
    if x.shape != b.shape:
        raise ValueError("x0 must have the same shape as b")
    return x.copy()


def _relative_residual_norm(A: Array, b: Array, x: Array) -> tuple[float, float]:
    residual_norm = float(np.linalg.norm(b - A @ x, ord=2))
    b_norm = float(np.linalg.norm(b, ord=2))
    if b_norm == 0.0:
        return residual_norm, residual_norm
    return residual_norm, residual_norm / b_norm


def _relative_step_norm(x_new: Array, x_old: Array) -> float:
    denominator = max(float(np.linalg.norm(x_new, ord=2)), 1.0)
    return float(np.linalg.norm(x_new - x_old, ord=2) / denominator)


def _result(
    method: str,
    A: Array,
    b: Array,
    x: Array,
    iterations: int,
    converged: bool,
    last_step_norm: float,
) -> IterationResult:
    residual_norm, relative_residual_norm = _relative_residual_norm(A, b, x)
    return IterationResult(
        method=method,
        x=x,
        iterations=iterations,
        converged=converged,
        residual_norm=residual_norm,
        relative_residual_norm=relative_residual_norm,
        last_step_norm=last_step_norm,
    )


def build_shifted_hilbert_system(n: int) -> tuple[Array, Array, Array]:
    """Build a_ij = 1/(i+j+1), b_i = one third of the row sum, 1-based i,j."""
    if n <= 0:
        raise ValueError("n must be positive")
    A = np.fromfunction(lambda i, j: 1.0 / (i + j + 3.0), (n, n), dtype=float)
    exact = np.full(n, 1.0 / 3.0, dtype=float)
    b = A @ exact
    return A, b, exact


def build_problem3_system() -> tuple[Array, Array, Array]:
    A = np.array(
        [
            [10.0, 1.0, 2.0, 3.0, 4.0],
            [1.0, 9.0, -1.0, 2.0, -3.0],
            [2.0, -1.0, 7.0, 3.0, -5.0],
            [3.0, 2.0, 3.0, 12.0, -1.0],
            [4.0, -3.0, -5.0, -1.0, 15.0],
        ],
        dtype=float,
    )
    b = np.array([12.0, -27.0, 14.0, -17.0, 12.0], dtype=float)
    exact = np.array([1.0, -2.0, 3.0, -2.0, 1.0], dtype=float)
    return A, b, exact


def jacobi(A: Array, b: Array, config: IterationConfig | None = None, x0: Array | None = None) -> IterationResult:
    """Jacobi iteration x_k = D^{-1}(L+U)x_{k-1}+D^{-1}b for Ax=b."""
    if config is None:
        config = IterationConfig()
    A, b = _as_system(A, b)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Jacobi iteration requires nonzero diagonal entries")

    x = _initial_guess(b, x0)
    rest = A - np.diag(diagonal)
    residual_norm, relative_residual_norm = _relative_residual_norm(A, b, x)
    last_step_norm = 0.0
    if relative_residual_norm <= config.tolerance:
        return _result("Jacobi", A, b, x, 0, True, last_step_norm)

    for iteration in range(1, config.max_iterations + 1):
        x_new = (b - rest @ x) / diagonal
        last_step_norm = _relative_step_norm(x_new, x)
        x = x_new
        residual_norm, relative_residual_norm = _relative_residual_norm(A, b, x)
        if relative_residual_norm <= config.tolerance:
            return _result("Jacobi", A, b, x, iteration, True, last_step_norm)

    return _result("Jacobi", A, b, x, config.max_iterations, False, last_step_norm)


def gauss_seidel(
    A: Array,
    b: Array,
    config: IterationConfig | None = None,
    x0: Array | None = None,
) -> IterationResult:
    """Gauss-Seidel iteration x_k = (D-L)^{-1}Ux_{k-1}+(D-L)^{-1}b."""
    if config is None:
        config = IterationConfig()
    A, b = _as_system(A, b)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Gauss-Seidel iteration requires nonzero diagonal entries")

    n = b.size
    x = _initial_guess(b, x0)
    residual_norm, relative_residual_norm = _relative_residual_norm(A, b, x)
    last_step_norm = 0.0
    if relative_residual_norm <= config.tolerance:
        return _result("Gauss-Seidel", A, b, x, 0, True, last_step_norm)

    for iteration in range(1, config.max_iterations + 1):
        x_old = x.copy()
        for i in range(n):
            left = A[i, :i] @ x[:i]
            right = A[i, i + 1 :] @ x_old[i + 1 :]
            x[i] = (b[i] - left - right) / A[i, i]
        last_step_norm = _relative_step_norm(x, x_old)
        residual_norm, relative_residual_norm = _relative_residual_norm(A, b, x)
        if relative_residual_norm <= config.tolerance:
            return _result("Gauss-Seidel", A, b, x, iteration, True, last_step_norm)

    return _result("Gauss-Seidel", A, b, x, config.max_iterations, False, last_step_norm)


def conjugate_gradient(
    A: Array,
    b: Array,
    config: IterationConfig | None = None,
    x0: Array | None = None,
) -> IterationResult:
    """Practical conjugate-gradient iteration for symmetric positive definite Ax=b."""
    if config is None:
        config = IterationConfig()
    A, b = _as_system(A, b)
    if not np.allclose(A, A.T, rtol=1e-12, atol=1e-14):
        raise np.linalg.LinAlgError("conjugate gradient requires a symmetric matrix")

    x = _initial_guess(b, x0)
    r = b - A @ x
    rho = float(r @ r)
    b_norm = float(np.linalg.norm(b, ord=2))
    if b_norm == 0.0:
        return _result("CG", A, b, x, 0, True, 0.0)
    if np.sqrt(rho) <= config.tolerance * b_norm:
        return _result("CG", A, b, x, 0, True, 0.0)

    p = np.zeros_like(b, dtype=float)
    last_step_norm = 0.0
    rho_old = rho
    for iteration in range(1, config.max_iterations + 1):
        if iteration == 1:
            p = r.copy()
        else:
            beta = rho / rho_old
            p = r + beta * p

        w = A @ p
        denominator = float(p @ w)
        if denominator <= 0.0:
            raise np.linalg.LinAlgError("conjugate gradient encountered a nonpositive p^T A p")
        alpha = rho / denominator
        x_old = x.copy()
        x = x + alpha * p
        r = r - alpha * w
        rho_old = rho
        rho = float(r @ r)
        last_step_norm = _relative_step_norm(x, x_old)
        if np.sqrt(rho) <= config.tolerance * b_norm:
            return _result("CG", A, b, x, iteration, True, last_step_norm)

    return _result("CG", A, b, x, config.max_iterations, False, last_step_norm)


def jacobi_iteration_matrix(A: Array) -> Array:
    A = np.asarray(A, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Jacobi iteration matrix requires nonzero diagonal entries")
    return -np.diag(1.0 / diagonal) @ (A - np.diag(diagonal))


def gauss_seidel_iteration_matrix(A: Array) -> Array:
    A = np.asarray(A, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be a square matrix")
    lower_with_diagonal = np.tril(A)
    upper = np.triu(A, k=1)
    return np.linalg.solve(lower_with_diagonal, -upper)


def spectral_radius(A: Array) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(A))))


def format_float(value: float, precision: int = 6) -> str:
    if value == 0.0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-3 or abs_value >= 1e4:
        return f"{value:.{precision}e}"
    return f"{value:.{precision}f}"


def run_hilbert_experiments(
    sizes: list[int] | None = None,
    config: IterationConfig | None = None,
) -> list[dict[str, object]]:
    if sizes is None:
        sizes = [4, 6, 8, 10, 12]
    if config is None:
        config = IterationConfig(tolerance=1e-10, max_iterations=500)

    rows: list[dict[str, object]] = []
    for n in sizes:
        A, b, exact = build_shifted_hilbert_system(n)
        result = conjugate_gradient(A, b, config)
        direct = np.linalg.solve(A, b)
        rows.append(
            {
                "n": n,
                "condition": float(np.linalg.cond(A)),
                "result": result,
                "solution_error": float(np.linalg.norm(result.x - exact, ord=np.inf)),
                "direct_error": float(np.linalg.norm(direct - exact, ord=np.inf)),
            }
        )
    return rows


def run_problem3_experiment(config: IterationConfig | None = None) -> dict[str, object]:
    if config is None:
        config = IterationConfig(tolerance=1e-10, max_iterations=10000)
    A, b, exact = build_problem3_system()
    direct = np.linalg.solve(A, b)
    results = [
        jacobi(A, b, config),
        gauss_seidel(A, b, config),
        conjugate_gradient(A, b, IterationConfig(config.tolerance, max_iterations=A.shape[0])),
    ]
    return {
        "A": A,
        "b": b,
        "exact": exact,
        "direct": direct,
        "condition": float(np.linalg.cond(A)),
        "jacobi_rho": spectral_radius(jacobi_iteration_matrix(A)),
        "gs_rho": spectral_radius(gauss_seidel_iteration_matrix(A)),
        "results": results,
        "errors": {result.method: float(np.linalg.norm(result.x - exact, ord=np.inf)) for result in results},
    }


def make_hilbert_markdown(rows: list[dict[str, object]]) -> str:
    lines = [
        "| n | cond_2(A) | iterations | converged | rel residual | residual 2 | ||x-x*||_inf | direct ||x-x*||_inf |",
        "|---:|---:|---:|:---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        result = row["result"]
        assert isinstance(result, IterationResult)
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["n"]),
                    format_float(float(row["condition"]), 3),
                    str(result.iterations),
                    "yes" if result.converged else "no",
                    format_float(result.relative_residual_norm, 3),
                    format_float(result.residual_norm, 3),
                    format_float(float(row["solution_error"]), 3),
                    format_float(float(row["direct_error"]), 3),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def make_problem3_markdown(case: dict[str, object]) -> str:
    lines = [
        "| method | iterations | converged | rel residual | residual 2 | ||x-x*||_inf | x |",
        "|:---|---:|:---:|---:|---:|---:|:---|",
    ]
    errors = case["errors"]
    for result in case["results"]:
        assert isinstance(result, IterationResult)
        x_text = "(" + ", ".join(f"{value:.10g}" for value in result.x) + ")"
        lines.append(
            "| "
            + " | ".join(
                [
                    result.method,
                    str(result.iterations),
                    "yes" if result.converged else "no",
                    format_float(result.relative_residual_norm, 3),
                    format_float(result.residual_norm, 3),
                    format_float(float(errors[result.method]), 3),
                    x_text,
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def write_hilbert_csv(rows: list[dict[str, object]], path: str | Path = "hw6_hilbert_results.csv") -> None:
    with Path(path).open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "n",
                "condition_2",
                "iterations",
                "converged",
                "relative_residual_2",
                "residual_2",
                "solution_error_inf",
                "direct_solution_error_inf",
            ]
        )
        for row in rows:
            result = row["result"]
            assert isinstance(result, IterationResult)
            writer.writerow(
                [
                    row["n"],
                    f"{float(row['condition']):.16e}",
                    result.iterations,
                    int(result.converged),
                    f"{result.relative_residual_norm:.16e}",
                    f"{result.residual_norm:.16e}",
                    f"{float(row['solution_error']):.16e}",
                    f"{float(row['direct_error']):.16e}",
                ]
            )


def main() -> None:
    hilbert_rows = run_hilbert_experiments()
    problem3_case = run_problem3_experiment()
    hilbert_table = make_hilbert_markdown(hilbert_rows)
    problem3_table = make_problem3_markdown(problem3_case)
    spectral_text = (
        f"Problem 3: cond_2(A)={problem3_case['condition']:.6g}, "
        f"rho(B_J)={problem3_case['jacobi_rho']:.6g}, "
        f"rho(B_GS)={problem3_case['gs_rho']:.6g}"
    )
    print(hilbert_table)
    print()
    print(spectral_text)
    print(problem3_table)
    Path("hw6_results.md").write_text(
        hilbert_table + "\n\n" + spectral_text + "\n\n" + problem3_table + "\n",
        encoding="utf-8",
    )
    write_hilbert_csv(hilbert_rows)


if __name__ == "__main__":
    main()
