from __future__ import annotations

from pathlib import Path

import numpy as np

from hw9 import (
    build_tridiagonal_toeplitz,
    eigenpair_residuals,
    jacobi_eigenpairs,
    off_diagonal_norm,
    run_all_cases,
    toeplitz_tridiagonal_exact_eigenpairs,
)


def test_jacobi_diagonalizes_small_symmetric_matrix() -> None:
    matrix = np.array(
        [
            [4.0, 1.0, 2.0],
            [1.0, 3.0, -1.0],
            [2.0, -1.0, 5.0],
        ],
        dtype=float,
    )

    result = jacobi_eigenpairs(matrix, tolerance=1e-13, max_sweeps=50)

    assert result.converged
    assert result.rotations > 0
    assert off_diagonal_norm(result.diagonalized_matrix) < 1e-12
    np.testing.assert_allclose(result.eigenvalues, np.linalg.eigvalsh(matrix), rtol=1e-11, atol=1e-11)
    np.testing.assert_allclose(result.eigenvectors.T @ result.eigenvectors, np.eye(3), rtol=1e-12, atol=1e-12)
    assert float(np.max(eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors))) < 1e-11


def test_jacobi_matches_toeplitz_closed_form_for_homework_matrix() -> None:
    n = 50
    matrix = build_tridiagonal_toeplitz(n, diagonal=4.0, off_diagonal=1.0)
    expected_values, expected_vectors = toeplitz_tridiagonal_exact_eigenpairs(n, diagonal=4.0, off_diagonal=1.0)

    result = jacobi_eigenpairs(matrix, tolerance=1e-12, max_sweeps=250)

    assert result.converged
    np.testing.assert_allclose(result.eigenvalues, expected_values, rtol=1e-10, atol=1e-10)
    for index in range(n):
        alignment = abs(float(result.eigenvectors[:, index] @ expected_vectors[:, index]))
        assert alignment > 1.0 - 1e-8
    assert float(np.max(eigenpair_residuals(matrix, result.eigenvalues, result.eigenvectors))) < 1e-9
    assert result.off_diagonal_norm < 1e-10


def test_run_all_cases_writes_hw9_artifacts(tmp_path: Path) -> None:
    outputs = run_all_cases(output_dir=tmp_path, sizes=[50, 51], tolerance=1e-12)

    expected_files = {
        "hw9_summary.csv",
        "hw9_eigenpairs.csv",
        "hw9_results.md",
    }

    assert expected_files.issubset({path.name for path in outputs})
    assert (tmp_path / "hw9_summary.csv").read_text(encoding="utf-8").count("\n") == 3
    assert (tmp_path / "hw9_eigenpairs.csv").read_text(encoding="utf-8").count("\n") == 102
    results_text = (tmp_path / "hw9_results.md").read_text(encoding="utf-8")
    assert "classic Jacobi" in results_text
    assert "n=50,...,100" in results_text
