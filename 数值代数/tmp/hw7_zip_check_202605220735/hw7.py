from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class PowerMethodResult:
    eigenvalue: complex
    eigenvector: Array
    iterations: int
    converged: bool
    residual_norm: float
    relative_residual_norm: float
    last_change: float
    reason: str


@dataclass(frozen=True)
class RootResult:
    root: complex
    iterations: int
    converged: bool
    residual: float
    relative_polynomial_residual: float
    matrix_residual_norm: float
    relative_matrix_residual_norm: float
    last_change: float
    reason: str


@dataclass(frozen=True)
class PolynomialCase:
    label: str
    coefficients: list[float]
    power_result: RootResult
    squared_power_result: RootResult | None
    reference_root: complex
    reference_roots: Array
    reference_modulus: float


def _clean_complex(value: complex, tolerance: float = 1e-12) -> complex:
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


def format_float(value: float, precision: int = 6) -> str:
    if value == 0.0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-3 or abs_value >= 1e4:
        return f"{value:.{precision}e}"
    return f"{value:.{precision}f}"


def evaluate_monic_polynomial(coefficients: list[float] | Array, x: complex) -> complex:
    """Evaluate x^n + a_{n-1} x^{n-1} + ... + a_0 by Horner's rule."""
    values = np.asarray(coefficients, dtype=np.complex128)
    result = 1.0 + 0.0j
    for coefficient in values:
        result = result * x + coefficient
    return complex(result)


def polynomial_residual(coefficients: list[float] | Array, x: complex) -> float:
    return abs(evaluate_monic_polynomial(coefficients, x))


def relative_polynomial_residual(coefficients: list[float] | Array, x: complex) -> float:
    """Return a componentwise-scaled polynomial residual."""
    coeffs = np.asarray(coefficients, dtype=float)
    n = coeffs.size
    abs_x = abs(x)
    scale = abs_x**n
    for j, coefficient in enumerate(coeffs):
        scale += abs(float(coefficient)) * abs_x ** (n - 1 - j)
    return polynomial_residual(coefficients, x) / max(float(scale), 1.0)


def companion_matrix(coefficients: list[float] | Array) -> Array:
    """Return the Frobenius companion matrix for a monic polynomial.

    For f(x)=x^n+a_{n-1}x^{n-1}+...+a_1x+a_0, the matrix is
        [0 1 0 ... 0]
        [0 0 1 ... 0]
        ...
        [-a_0 -a_1 ... -a_{n-1}]
    and det(xI-C)=f(x).
    """
    coeffs = np.asarray(coefficients, dtype=float)
    if coeffs.ndim != 1 or coeffs.size == 0:
        raise ValueError("coefficients must be a nonempty one-dimensional array")
    n = coeffs.size
    matrix = np.zeros((n, n), dtype=float)
    if n > 1:
        matrix[:-1, 1:] = np.eye(n - 1, dtype=float)
    matrix[-1, :] = -coeffs[::-1]
    return matrix


def _default_initial_vector(n: int, dtype: np.dtype | type = np.float64) -> Array:
    # Use a deterministic vector with nonzero components to avoid accidentally
    # starting in an invariant subspace for companion matrices.
    return np.linspace(1.0, 2.0, n, dtype=float).astype(dtype)


def _max_abs_component_index(vector: Array) -> int:
    return int(np.argmax(np.abs(vector)))


def _relative_vector_change(new: Array, old: Array) -> float:
    denominator = max(float(np.linalg.norm(new, ord=np.inf)), 1.0)
    return float(np.linalg.norm(new - old, ord=np.inf) / denominator)


def _relative_eigen_residual(A: Array, eigenvalue: complex, eigenvector: Array) -> tuple[float, float]:
    residual = A @ eigenvector - eigenvalue * eigenvector
    residual_norm = float(np.linalg.norm(residual, ord=np.inf))
    denominator = max(float(np.linalg.norm(A, ord=np.inf) * np.linalg.norm(eigenvector, ord=np.inf)), 1.0)
    return residual_norm, residual_norm / denominator


def power_method_dominant_eigenvalue(
    A: Array,
    tolerance: float = 1e-12,
    max_iterations: int = 10000,
    u0: Array | None = None,
    stagnation_window: int = 20,
) -> PowerMethodResult:
    """Textbook power method with infinity-norm scaling.

    The iteration follows y_k=A u_{k-1}, mu_k=(a component of y_k with
    largest modulus), u_k=y_k/mu_k.  Convergence is accepted only when both
    the eigenvalue estimate and the normalized vector become stable.
    """
    matrix = np.asarray(A)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("A must be a square matrix")
    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")
    if max_iterations <= 0:
        raise ValueError("max_iterations must be positive")

    use_complex = np.iscomplexobj(matrix) or (u0 is not None and np.iscomplexobj(u0))
    dtype = np.complex128 if use_complex else np.float64
    matrix = matrix.astype(dtype, copy=False)

    if u0 is None:
        u = _default_initial_vector(matrix.shape[0], dtype=dtype)
    else:
        u = np.asarray(u0, dtype=dtype).copy()
        if u.shape != (matrix.shape[0],):
            raise ValueError("u0 must have length matching A")
    if np.linalg.norm(u, ord=np.inf) == 0.0:
        raise ValueError("u0 must be nonzero")
    scale_index = _max_abs_component_index(u)
    u = u / u[scale_index]

    mu_old: complex | None = None
    last_change = float("inf")
    recent_changes: list[float] = []
    mu = complex("nan")

    for iteration in range(1, max_iterations + 1):
        y = matrix @ u
        scale_index = _max_abs_component_index(y)
        mu = complex(y[scale_index])
        if abs(mu) == 0.0:
            residual_norm, relative_residual_norm = _relative_eigen_residual(matrix, 0.0, u)
            return PowerMethodResult(
                eigenvalue=0.0,
                eigenvector=u,
                iterations=iteration,
                converged=False,
                residual_norm=residual_norm,
                relative_residual_norm=relative_residual_norm,
                last_change=float("inf"),
                reason="zero scaling component",
            )

        u_new = y / mu
        vector_change = _relative_vector_change(u_new, u)
        if mu_old is None:
            eigenvalue_change = float("inf")
        else:
            eigenvalue_change = abs(mu - mu_old) / max(abs(mu), 1.0)
        last_change = max(vector_change, float(eigenvalue_change))
        residual_norm, relative_residual_norm = _relative_eigen_residual(matrix, mu, u_new)

        if (
            last_change <= tolerance
            and relative_residual_norm <= max(100.0 * tolerance, 1e-14)
        ):
            return PowerMethodResult(
                eigenvalue=_clean_complex(mu),
                eigenvector=u_new,
                iterations=iteration,
                converged=True,
                residual_norm=residual_norm,
                relative_residual_norm=relative_residual_norm,
                last_change=last_change,
                reason="converged",
            )

        recent_changes.append(last_change)
        if len(recent_changes) > stagnation_window:
            recent_changes.pop(0)

        u = u_new
        mu_old = mu

    residual_norm, relative_residual_norm = _relative_eigen_residual(matrix, mu, u)
    if recent_changes and min(recent_changes) > 1e-3:
        reason = "not converged; dominant roots may have equal modulus"
    else:
        reason = "maximum iterations reached"
    return PowerMethodResult(
        eigenvalue=_clean_complex(mu),
        eigenvector=u,
        iterations=max_iterations,
        converged=False,
        residual_norm=residual_norm,
        relative_residual_norm=relative_residual_norm,
        last_change=last_change,
        reason=reason,
    )


def modulus_largest_root(
    coefficients: list[float] | Array,
    tolerance: float = 1e-12,
    max_iterations: int = 10000,
    u0: Array | None = None,
    square_matrix: bool = False,
) -> RootResult:
    matrix = companion_matrix(coefficients)
    working_matrix = matrix @ matrix if square_matrix else matrix
    eigen_result = power_method_dominant_eigenvalue(
        working_matrix,
        tolerance=tolerance,
        max_iterations=max_iterations,
        u0=u0,
    )
    root = eigen_result.eigenvalue
    if square_matrix and eigen_result.converged:
        root = _choose_root_from_squared_value(coefficients, eigen_result.eigenvalue)
    residual = polynomial_residual(coefficients, root)
    scaled_residual = relative_polynomial_residual(coefficients, root)
    matrix_residual_norm, relative_matrix_residual_norm = _relative_eigen_residual(matrix, root, eigen_result.eigenvector)
    return RootResult(
        root=_clean_complex(root),
        iterations=eigen_result.iterations,
        converged=eigen_result.converged,
        residual=residual,
        relative_polynomial_residual=scaled_residual,
        matrix_residual_norm=matrix_residual_norm,
        relative_matrix_residual_norm=relative_matrix_residual_norm,
        last_change=eigen_result.last_change,
        reason=eigen_result.reason,
    )


def _choose_root_from_squared_value(coefficients: list[float] | Array, squared_value: complex) -> complex:
    candidates = [np.sqrt(squared_value), -np.sqrt(squared_value)]
    if abs(squared_value.imag) < 1e-12 and squared_value.real < 0.0:
        imag = np.sqrt(abs(squared_value.real))
        candidates = [1j * imag, -1j * imag]
    return min(candidates, key=lambda z: polynomial_residual(coefficients, z))


def reference_roots(coefficients: list[float] | Array) -> Array:
    polynomial_coefficients = np.array([1.0, *np.asarray(coefficients, dtype=float)], dtype=float)
    return np.roots(polynomial_coefficients)


def select_reference_modulus_largest_root(coefficients: list[float] | Array) -> tuple[complex, Array, float]:
    roots = reference_roots(coefficients)
    moduli = np.abs(roots)
    modulus = float(np.max(moduli))
    candidates = roots[np.isclose(moduli, modulus, rtol=1e-10, atol=1e-10)]
    # Deterministic display choice: largest real part, then largest imaginary part.
    ordered = sorted((complex(root) for root in candidates), key=lambda z: (z.real, z.imag), reverse=True)
    return _clean_complex(ordered[0]), roots, modulus


def problem_cases() -> list[tuple[str, list[float]]]:
    return [
        ("(i)", [1.0, -5.0, 3.0]),
        ("(ii)", [0.0, -3.0, -1.0]),
        ("(iii)", [101.0, 208.01, 10891.01, 9802.08, 79108.9, -99902.0, 790.0, -1000.0]),
    ]


def run_case(
    label: str,
    coefficients: list[float],
    tolerance: float = 1e-12,
    max_iterations: int = 20000,
) -> PolynomialCase:
    power_result = modulus_largest_root(coefficients, tolerance=tolerance, max_iterations=max_iterations)
    squared_power_result: RootResult | None = None
    if not power_result.converged:
        squared_power_result = modulus_largest_root(
            coefficients,
            tolerance=tolerance,
            max_iterations=max_iterations,
            square_matrix=True,
        )
    reference_root, roots, reference_modulus = select_reference_modulus_largest_root(coefficients)
    return PolynomialCase(
        label=label,
        coefficients=coefficients,
        power_result=power_result,
        squared_power_result=squared_power_result,
        reference_root=reference_root,
        reference_roots=roots,
        reference_modulus=reference_modulus,
    )


def run_all_cases() -> list[PolynomialCase]:
    return [run_case(label, coefficients) for label, coefficients in problem_cases()]


def make_markdown_table(rows: list[PolynomialCase]) -> str:
    lines = [
        "| case | n | power root | converged | iterations | scaled residual | matrix rel residual | reference modulus | selected reference root | note |",
        "|:---:|---:|---:|:---:|---:|---:|---:|---:|---:|:---|",
    ]
    for row in rows:
        power = row.power_result
        note = power.reason
        root = power.root
        scaled_residual = power.relative_polynomial_residual
        matrix_residual = power.relative_matrix_residual_norm
        iterations = power.iterations
        converged = "yes" if power.converged else "no"
        if (not power.converged) and row.squared_power_result is not None:
            squared = row.squared_power_result
            root = squared.root
            scaled_residual = squared.relative_polynomial_residual
            matrix_residual = squared.relative_matrix_residual_norm
            iterations = squared.iterations
            converged = "A^2 yes" if squared.converged else "no"
            note = f"plain power: {power.reason}; displayed root from A^2"
        lines.append(
            "| "
            + " | ".join(
                [
                    row.label,
                    str(len(row.coefficients)),
                    format_complex(root, 12),
                    converged,
                    str(iterations),
                    format_float(float(scaled_residual), 3),
                    format_float(float(matrix_residual), 3),
                    format_float(row.reference_modulus, 12),
                    format_complex(row.reference_root, 12),
                    note,
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def write_results_csv(rows: list[PolynomialCase], path: str | Path = "hw7_results.csv") -> None:
    with Path(path).open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "case",
                "degree",
                "plain_power_root",
                "plain_power_converged",
                "plain_power_iterations",
                "plain_power_abs_f",
                "plain_power_scaled_residual",
                "plain_power_matrix_rel_residual",
                "plain_power_reason",
                "reported_root",
                "reported_abs_f",
                "reported_scaled_residual",
                "reported_matrix_rel_residual",
                "reported_source",
                "reference_modulus",
                "selected_reference_root",
                "all_reference_roots",
            ]
        )
        for row in rows:
            reported = row.power_result
            source = "plain power"
            if (not reported.converged) and row.squared_power_result is not None:
                reported = row.squared_power_result
                source = "power method on A^2"
            writer.writerow(
                [
                    row.label,
                    len(row.coefficients),
                    format_complex(row.power_result.root, 16),
                    int(row.power_result.converged),
                    row.power_result.iterations,
                    f"{row.power_result.residual:.16e}",
                    f"{row.power_result.relative_polynomial_residual:.16e}",
                    f"{row.power_result.relative_matrix_residual_norm:.16e}",
                    row.power_result.reason,
                    format_complex(reported.root, 16),
                    f"{reported.residual:.16e}",
                    f"{reported.relative_polynomial_residual:.16e}",
                    f"{reported.relative_matrix_residual_norm:.16e}",
                    source,
                    f"{row.reference_modulus:.16e}",
                    format_complex(row.reference_root, 16),
                    "; ".join(format_complex(root, 16) for root in row.reference_roots),
                ]
            )


def make_results_markdown(rows: list[PolynomialCase]) -> str:
    lines = [make_markdown_table(rows), "", "Reference roots:"]
    for row in rows:
        roots = ", ".join(format_complex(root, 12) for root in row.reference_roots)
        lines.append(f"- {row.label}: {roots}")
        if row.squared_power_result is not None:
            lines.append(
                f"  A^2 check: root={format_complex(row.squared_power_result.root, 12)}, "
                f"converged={row.squared_power_result.converged}, "
                f"iterations={row.squared_power_result.iterations}, "
                f"|f|={row.squared_power_result.residual:.3e}"
            )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = run_all_cases()
    markdown = make_results_markdown(rows)
    print(markdown)
    Path("hw7_results.md").write_text(markdown, encoding="utf-8")
    write_results_csv(rows)


if __name__ == "__main__":
    main()
