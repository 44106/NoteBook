from __future__ import annotations

from pathlib import Path

import numpy as np

from hw8 import (
    build_tridiagonal_toeplitz,
    companion_matrix_for_monic_polynomial,
    eigenpair_residuals,
    implicit_qr_eigenpairs,
    polynomial_roots_by_implicit_qr,
    run_all_cases,
    symmetric_qr_eigenpairs,
)


def _sort_complex(values: np.ndarray) -> np.ndarray:
    return np.array(sorted(values, key=lambda z: (round(float(np.real(z)), 12), round(float(np.imag(z)), 12))))


def test_general_implicit_qr_matches_numpy_on_real_matrix() -> None:
    matrix = np.array(
        [
            [9.1, 3.0, 2.6, 4.0],
            [4.2, 5.3, 4.7, 1.6],
            [3.2, 1.7, 9.4, 1.0],
            [6.1, 4.9, 3.5, 6.2],
        ],
        dtype=float,
    )

    result = implicit_qr_eigenpairs(matrix, tolerance=1e-12, max_iterations=20_000)

    assert result.converged
    np.testing.assert_allclose(
        _sort_complex(result.eigenvalues),
        _sort_complex(np.linalg.eigvals(matrix)),
        rtol=1e-9,
        atol=1e-10,
    )
    assert float(np.max(eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors))) < 1e-8


def test_companion_roots_for_x41_plus_x3_plus_one_match_numpy_roots() -> None:
    coefficients = [0.0] * 42
    coefficients[0] = 1.0
    coefficients[38] = 1.0
    coefficients[41] = 1.0

    result = polynomial_roots_by_implicit_qr(coefficients, tolerance=1e-12, max_iterations=60_000)
    expected = np.roots(coefficients)

    assert result.converged
    assert result.roots.shape == (41,)
    np.testing.assert_allclose(
        _sort_complex(result.roots),
        _sort_complex(expected),
        rtol=5e-9,
        atol=5e-10,
    )
    assert float(np.max(result.scaled_residuals)) < 1e-9


def test_companion_matrix_represents_monic_polynomial() -> None:
    # x^4 + 2 x^2 - 3 x + 5
    coefficients = [1.0, 0.0, 2.0, -3.0, 5.0]
    companion = companion_matrix_for_monic_polynomial(coefficients)

    assert companion.shape == (4, 4)
    np.testing.assert_allclose(np.poly(companion), coefficients, rtol=1e-12, atol=1e-12)


def test_symmetric_qr_matches_exact_toeplitz_eigenpairs() -> None:
    n = 18
    matrix = build_tridiagonal_toeplitz(n, diagonal=4.0, off_diagonal=1.0)
    result = symmetric_qr_eigenpairs(matrix, tolerance=1e-13, max_iterations=40_000)
    k = np.arange(1, n + 1, dtype=float)
    expected = 4.0 + 2.0 * np.cos(k * np.pi / (n + 1.0))

    assert result.converged
    np.testing.assert_allclose(np.sort(result.eigenvalues), np.sort(expected), rtol=1e-11, atol=1e-11)
    assert float(np.max(eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors))) < 1e-10
    np.testing.assert_allclose(result.eigenvectors.T @ result.eigenvectors, np.eye(n), rtol=1e-11, atol=1e-11)


def test_symmetric_qr_extreme_values_for_laplacian_matrix() -> None:
    n = 100
    matrix = build_tridiagonal_toeplitz(n, diagonal=2.0, off_diagonal=-1.0)
    result = symmetric_qr_eigenpairs(matrix, tolerance=1e-13, max_iterations=80_000)

    expected_min = 2.0 - 2.0 * np.cos(np.pi / (n + 1.0))
    expected_max = 2.0 - 2.0 * np.cos(n * np.pi / (n + 1.0))

    assert result.converged
    assert abs(float(np.min(result.eigenvalues)) - expected_min) < 1e-10
    assert abs(float(np.max(result.eigenvalues)) - expected_max) < 1e-10
    assert float(np.max(eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors))) < 1e-9


def test_run_all_cases_writes_expected_artifacts(tmp_path: Path) -> None:
    outputs = run_all_cases(output_dir=tmp_path, p244_1_sizes=[50, 51], tolerance=1e-12)

    expected_files = {
        "hw8_p202_roots.csv",
        "hw8_p202_matrix_eigenpairs.csv",
        "hw8_p244_1_summary.csv",
        "hw8_p244_1_eigenpairs.csv",
        "hw8_p244_2_eigenpairs.csv",
        "hw8_results.md",
    }

    assert expected_files.issubset({path.name for path in outputs})
    assert (tmp_path / "hw8_p202_roots.csv").read_text(encoding="utf-8").count("\n") == 42
    assert (tmp_path / "hw8_p244_1_summary.csv").read_text(encoding="utf-8").count("\n") == 3
