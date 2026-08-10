import numpy as np

from hw7 import (
    companion_matrix,
    evaluate_monic_polynomial,
    modulus_largest_root,
    power_method_dominant_eigenvalue,
    polynomial_residual,
    run_all_cases,
)


def test_companion_matrix_has_given_monic_polynomial() -> None:
    # f(x) = x^3 + x^2 - 5x + 3 = (x - 1)^2 (x + 3)
    coefficients = [1.0, -5.0, 3.0]
    C = companion_matrix(coefficients)

    assert C.shape == (3, 3)
    computed = np.poly(C)
    expected = np.array([1.0, 1.0, -5.0, 3.0])
    np.testing.assert_allclose(computed, expected, rtol=1e-12, atol=1e-12)


def test_power_method_finds_simple_real_dominant_root() -> None:
    coefficients = [1.0, -5.0, 3.0]
    result = modulus_largest_root(coefficients, tolerance=1e-12, max_iterations=1000)

    assert result.converged
    assert abs(result.root + 3.0) < 1e-10
    assert polynomial_residual(coefficients, result.root) < 1e-9


def test_power_method_detects_nonconvergence_for_equal_modulus_roots() -> None:
    coefficients = [0.0, -4.0, 0.0]
    result = modulus_largest_root(coefficients, tolerance=1e-12, max_iterations=80)

    assert not result.converged
    roots = np.roots([1.0, *coefficients])
    assert np.count_nonzero(np.isclose(np.abs(roots), 2.0)) == 2


def test_case_results_match_reference_roots() -> None:
    rows = run_all_cases()

    assert len(rows) == 3
    case1, case2, case3 = rows

    assert case1.power_result.converged
    assert abs(case1.power_result.root - case1.reference_root) < 1e-8
    assert abs(case1.reference_root + 3.0) < 1e-12

    assert case2.power_result.converged
    assert abs(case2.power_result.root - case2.reference_root) < 1e-8
    assert abs(case2.reference_root - 1.8793852415718169) < 1e-12

    assert case3.power_result.converged
    assert abs(case3.power_result.root - case3.reference_root) < 1e-8
    assert case3.power_result.relative_polynomial_residual < 1e-14
    assert case3.power_result.relative_matrix_residual_norm < 1e-14


def test_complex_power_method_handles_complex_dominant_eigenvalue() -> None:
    A = np.array([[0.0, -2.0], [2.0, 0.0]])
    result = power_method_dominant_eigenvalue(A, tolerance=1e-12, max_iterations=20)

    assert not result.converged
    assert np.isfinite(abs(result.eigenvalue))
