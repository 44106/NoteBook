import numpy as np

from hw6 import (
    IterationConfig,
    build_problem3_system,
    build_shifted_hilbert_system,
    conjugate_gradient,
    gauss_seidel,
    gauss_seidel_iteration_matrix,
    jacobi,
    jacobi_iteration_matrix,
    spectral_radius,
)


def test_shifted_hilbert_system_has_one_third_solution():
    A, b, exact = build_shifted_hilbert_system(6)

    expected_A = np.fromfunction(lambda i, j: 1.0 / (i + j + 3.0), (6, 6))

    assert np.allclose(A, expected_A)
    assert np.allclose(exact, np.full(6, 1.0 / 3.0))
    assert np.allclose(A @ exact, b, rtol=1e-14, atol=1e-14)


def test_iterative_methods_match_direct_solution_on_spd_system():
    A = np.array(
        [
            [4.0, 1.0, 0.0],
            [1.0, 3.0, 1.0],
            [0.0, 1.0, 2.0],
        ]
    )
    b = np.array([1.0, 2.0, 3.0])
    expected = np.linalg.solve(A, b)
    config = IterationConfig(tolerance=1e-12, max_iterations=10000)

    jacobi_result = jacobi(A, b, config)
    gs_result = gauss_seidel(A, b, config)
    cg_result = conjugate_gradient(A, b, config)

    assert jacobi_result.converged
    assert gs_result.converged
    assert cg_result.converged
    assert np.allclose(jacobi_result.x, expected, rtol=1e-10, atol=1e-10)
    assert np.allclose(gs_result.x, expected, rtol=1e-10, atol=1e-10)
    assert np.allclose(cg_result.x, expected, rtol=1e-10, atol=1e-10)


def test_problem3_matrix_has_convergent_stationary_iteration_matrices():
    A, b, _ = build_problem3_system()

    jacobi_rho = spectral_radius(jacobi_iteration_matrix(A))
    gs_rho = spectral_radius(gauss_seidel_iteration_matrix(A))

    assert b.shape == (5,)
    assert np.allclose(A, A.T)
    assert jacobi_rho < 1.0
    assert gs_rho < 1.0
    assert gs_rho < jacobi_rho


def test_problem3_cg_reaches_direct_solution_in_at_most_five_steps():
    A, b, _ = build_problem3_system()
    expected = np.linalg.solve(A, b)
    config = IterationConfig(tolerance=1e-12, max_iterations=5)

    result = conjugate_gradient(A, b, config)

    assert result.converged
    assert result.iterations <= 5
    assert np.allclose(result.x, expected, rtol=1e-10, atol=1e-10)
