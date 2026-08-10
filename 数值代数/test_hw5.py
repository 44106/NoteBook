import numpy as np

from hw5 import (
    IterationConfig,
    build_bvp_system,
    exact_solution,
    gauss_seidel,
    jacobi,
    sor,
)


def test_exact_solution_satisfies_boundary_values():
    eps = 0.1
    a = 0.5

    values = exact_solution(np.array([0.0, 1.0]), eps, a)

    assert np.allclose(values, np.array([0.0, 1.0]), rtol=1e-13, atol=1e-13)


def test_build_bvp_system_includes_right_boundary_contribution():
    eps = 0.1
    a = 0.5
    n = 4
    h = 1.0 / n

    A, b, x = build_bvp_system(eps, a, n)

    expected_A = np.array(
        [
            [2 * eps + h, -(eps + h), 0.0],
            [-eps, 2 * eps + h, -(eps + h)],
            [0.0, -eps, 2 * eps + h],
        ]
    )
    expected_b = np.array([-a * h * h, -a * h * h, eps + h - a * h * h])

    assert np.allclose(A, expected_A)
    assert np.allclose(b, expected_b)
    assert np.allclose(x, np.array([0.25, 0.5, 0.75]))


def test_stationary_iterations_match_direct_solution():
    A, b, _ = build_bvp_system(eps=0.1, a=0.5, n=12)
    expected = np.linalg.solve(A, b)
    config = IterationConfig(tolerance=1e-11, max_iterations=200000)

    jacobi_result = jacobi(A, b, config)
    gs_result = gauss_seidel(A, b, config)
    sor_result = sor(A, b, omega=1.2, config=config)

    assert jacobi_result.converged
    assert gs_result.converged
    assert sor_result.converged
    assert np.allclose(jacobi_result.x, expected, rtol=1e-9, atol=1e-10)
    assert np.allclose(gs_result.x, expected, rtol=1e-9, atol=1e-10)
    assert np.allclose(sor_result.x, expected, rtol=1e-9, atol=1e-10)
