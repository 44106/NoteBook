from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class IterationConfig:
    tolerance: float = 1e-10
    max_iterations: int = 2_000_000


@dataclass(frozen=True)
class IterationResult:
    method: str
    x: Array
    iterations: int
    converged: bool
    last_step_norm: float
    residual_norm: float
    omega: float | None = None


def exact_solution(x: Array | float, eps: float, a: float) -> Array | float:
    """Exact solution of eps*y'' + y' = a, y(0)=0, y(1)=1."""
    x_arr = np.asarray(x, dtype=float)
    denominator = 1.0 - np.exp(-1.0 / eps)
    values = ((1.0 - a) / denominator) * (1.0 - np.exp(-x_arr / eps)) + a * x_arr
    if np.isscalar(x):
        return float(values)
    return values


def build_bvp_system(eps: float, a: float, n: int) -> tuple[Array, Array, Array]:
    """Build the finite-difference system for the n-interval BVP discretization.

    The textbook discretization gives
        (eps+h)y_{i+1} -(2eps+h)y_i + eps*y_{i-1} = a h^2.
    Multiplying by -1 produces an equivalent system with positive diagonal.
    """
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    if not (0.0 < a < 1.0):
        raise ValueError("a must satisfy 0 < a < 1")
    if n < 2:
        raise ValueError("n must be at least 2")

    h = 1.0 / n
    size = n - 1
    diagonal = np.full(size, 2.0 * eps + h, dtype=float)
    lower = np.full(size - 1, -eps, dtype=float)
    upper = np.full(size - 1, -(eps + h), dtype=float)

    A = np.diag(diagonal)
    if size > 1:
        A += np.diag(lower, k=-1)
        A += np.diag(upper, k=1)

    b = np.full(size, -a * h * h, dtype=float)
    b[-1] += eps + h
    grid = h * np.arange(1, n, dtype=float)
    return A, b, grid


def _initial_guess(b: Array, x0: Array | None) -> Array:
    if x0 is None:
        return np.zeros_like(b, dtype=float)
    x = np.asarray(x0, dtype=float)
    if x.shape != b.shape:
        raise ValueError("x0 must have the same shape as b")
    return x.copy()


def _relative_step_norm(x_new: Array, x_old: Array) -> float:
    denominator = max(np.linalg.norm(x_new, ord=np.inf), 1.0)
    return float(np.linalg.norm(x_new - x_old, ord=np.inf) / denominator)


def _result(
    method: str,
    A: Array,
    b: Array,
    x: Array,
    iterations: int,
    converged: bool,
    last_step_norm: float,
    omega: float | None = None,
) -> IterationResult:
    residual_norm = float(np.linalg.norm(b - A @ x, ord=np.inf))
    return IterationResult(
        method=method,
        x=x,
        iterations=iterations,
        converged=converged,
        last_step_norm=last_step_norm,
        residual_norm=residual_norm,
        omega=omega,
    )


def jacobi(A: Array, b: Array, config: IterationConfig | None = None, x0: Array | None = None) -> IterationResult:
    """Jacobi iteration for Ax=b."""
    if config is None:
        config = IterationConfig()
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Jacobi iteration requires nonzero diagonal entries")

    x = _initial_guess(b, x0)
    rest = A - np.diag(diagonal)
    last_step = float("inf")
    for iteration in range(1, config.max_iterations + 1):
        x_new = (b - rest @ x) / diagonal
        last_step = _relative_step_norm(x_new, x)
        x = x_new
        if last_step < config.tolerance:
            return _result("Jacobi", A, b, x, iteration, True, last_step)
    return _result("Jacobi", A, b, x, config.max_iterations, False, last_step)


def gauss_seidel(
    A: Array,
    b: Array,
    config: IterationConfig | None = None,
    x0: Array | None = None,
) -> IterationResult:
    """Gauss-Seidel iteration for Ax=b."""
    if config is None:
        config = IterationConfig()
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Gauss-Seidel iteration requires nonzero diagonal entries")

    n = b.size
    x = _initial_guess(b, x0)
    last_step = float("inf")
    for iteration in range(1, config.max_iterations + 1):
        x_old = x.copy()
        for i in range(n):
            left = A[i, :i] @ x[:i]
            right = A[i, i + 1 :] @ x_old[i + 1 :]
            x[i] = (b[i] - left - right) / A[i, i]
        last_step = _relative_step_norm(x, x_old)
        if last_step < config.tolerance:
            return _result("Gauss-Seidel", A, b, x, iteration, True, last_step)
    return _result("Gauss-Seidel", A, b, x, config.max_iterations, False, last_step)


def sor(
    A: Array,
    b: Array,
    omega: float,
    config: IterationConfig | None = None,
    x0: Array | None = None,
) -> IterationResult:
    """Successive over-relaxation iteration for Ax=b."""
    if not (0.0 < omega < 2.0):
        raise ValueError("SOR omega must satisfy 0 < omega < 2")
    if config is None:
        config = IterationConfig()
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("SOR iteration requires nonzero diagonal entries")

    n = b.size
    x = _initial_guess(b, x0)
    last_step = float("inf")
    for iteration in range(1, config.max_iterations + 1):
        x_old = x.copy()
        for i in range(n):
            left = A[i, :i] @ x[:i]
            right = A[i, i + 1 :] @ x_old[i + 1 :]
            gs_value = (b[i] - left - right) / A[i, i]
            x[i] = (1.0 - omega) * x_old[i] + omega * gs_value
        last_step = _relative_step_norm(x, x_old)
        if last_step < config.tolerance:
            return _result("SOR", A, b, x, iteration, True, last_step, omega=omega)
    return _result("SOR", A, b, x, config.max_iterations, False, last_step, omega=omega)


def jacobi_iteration_matrix(A: Array) -> Array:
    A = np.asarray(A, dtype=float)
    diagonal = np.diag(A)
    if np.any(diagonal == 0.0):
        raise np.linalg.LinAlgError("Jacobi iteration matrix requires nonzero diagonal entries")
    return -np.diag(1.0 / diagonal) @ (A - np.diag(diagonal))


def spectral_radius(A: Array) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(A))))


def optimal_sor_omega(A: Array) -> float:
    """Return the classical omega_opt from the Jacobi spectral radius."""
    rho = spectral_radius(jacobi_iteration_matrix(A))
    if rho >= 1.0:
        raise ValueError("Jacobi spectral radius must be below 1 for this omega formula")
    return float(2.0 / (1.0 + np.sqrt(1.0 - rho * rho)))


def max_error_against_exact(x_numeric: Array, grid: Array, eps: float, a: float) -> float:
    y_exact = exact_solution(grid, eps, a)
    return float(np.linalg.norm(x_numeric - y_exact, ord=np.inf))


def significant_digit_error_bound(values: Array, exact: Array, digits: int = 4) -> bool:
    scale = np.maximum(np.abs(exact), 1.0)
    return bool(np.all(np.abs(values - exact) <= 0.5 * 10.0 ** (-digits) * scale))


def run_case(eps: float, a: float = 0.5, n: int = 100, config: IterationConfig | None = None) -> dict[str, object]:
    if config is None:
        config = IterationConfig()
    A, b, grid = build_bvp_system(eps, a, n)
    omega = optimal_sor_omega(A)
    results = [
        jacobi(A, b, config),
        gauss_seidel(A, b, config),
        sor(A, b, omega, config),
    ]
    exact = exact_solution(grid, eps, a)
    direct = np.linalg.solve(A, b)
    return {
        "eps": eps,
        "a": a,
        "n": n,
        "h": 1.0 / n,
        "omega": omega,
        "jacobi_rho": spectral_radius(jacobi_iteration_matrix(A)),
        "results": results,
        "linear_errors": {result.method: float(np.linalg.norm(result.x - direct, ord=np.inf)) for result in results},
        "exact_errors": {result.method: max_error_against_exact(result.x, grid, eps, a) for result in results},
        "four_digit_flags": {
            result.method: significant_digit_error_bound(result.x, direct, digits=4) for result in results
        },
        "direct_solution": direct,
        "direct_max_error": max_error_against_exact(direct, grid, eps, a),
        "exact_solution": exact,
    }


def format_float(value: float, precision: int = 6) -> str:
    if value == 0.0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-3 or abs_value >= 1e4:
        return f"{value:.{precision}e}"
    return f"{value:.{precision}f}"


def make_markdown_table(cases: list[dict[str, object]]) -> str:
    lines = [
        "| epsilon | method | omega | iterations | converged | step norm | residual inf | linear err inf | exact err inf | 4 digits for linear system |",
        "|---:|:---|---:|---:|:---:|---:|---:|---:|---:|:---:|",
    ]
    for case in cases:
        eps = float(case["eps"])
        linear_errors = case["linear_errors"]
        exact_errors = case["exact_errors"]
        four_digit_flags = case["four_digit_flags"]
        for result in case["results"]:
            assert isinstance(result, IterationResult)
            omega = "" if result.omega is None else f"{result.omega:.6f}"
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"{eps:g}",
                        result.method,
                        omega,
                        str(result.iterations),
                        "yes" if result.converged else "no",
                        format_float(result.last_step_norm, 3),
                        format_float(result.residual_norm, 3),
                        format_float(linear_errors[result.method], 3),
                        format_float(exact_errors[result.method], 3),
                        "yes" if four_digit_flags[result.method] else "no",
                    ]
                )
                + " |"
            )
    return "\n".join(lines)


def make_sample_table(cases: list[dict[str, object]], indices: list[int] | None = None) -> str:
    if indices is None:
        indices = [1, 25, 50, 75, 99]
    lines = [
        "| epsilon | i | x_i | SOR y_i | exact y(x_i) | abs error |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for case in cases:
        eps = float(case["eps"])
        h = float(case["h"])
        sor_result = next(result for result in case["results"] if isinstance(result, IterationResult) and result.method == "SOR")
        exact = case["exact_solution"]
        for i in indices:
            position = i - 1
            value = sor_result.x[position]
            exact_value = exact[position]
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"{eps:g}",
                        str(i),
                        f"{i * h:.2f}",
                        f"{value:.6g}",
                        f"{exact_value:.6g}",
                        format_float(abs(value - exact_value), 3),
                    ]
                )
                + " |"
            )
    return "\n".join(lines)


def write_solution_csv(cases: list[dict[str, object]], path: str | Path = "hw5_solution_values.csv") -> None:
    with Path(path).open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["epsilon", "i", "x_i", "exact", "Jacobi", "Gauss-Seidel", "SOR"])
        for case in cases:
            eps = float(case["eps"])
            h = float(case["h"])
            results = {result.method: result for result in case["results"] if isinstance(result, IterationResult)}
            exact = case["exact_solution"]
            for position, exact_value in enumerate(exact, start=1):
                writer.writerow(
                    [
                        f"{eps:g}",
                        position,
                        f"{position * h:.12g}",
                        f"{exact_value:.12g}",
                        f"{results['Jacobi'].x[position - 1]:.12g}",
                        f"{results['Gauss-Seidel'].x[position - 1]:.12g}",
                        f"{results['SOR'].x[position - 1]:.12g}",
                    ]
                )


def main() -> None:
    eps_values = [1.0, 0.1, 0.01, 0.0001]
    cases = [run_case(eps) for eps in eps_values]
    table = make_markdown_table(cases)
    samples = make_sample_table(cases)
    print(table)
    print()
    print(samples)
    Path("hw5_results.md").write_text(table + "\n\n" + samples + "\n", encoding="utf-8")
    write_solution_csv(cases)


if __name__ == "__main__":
    main()
