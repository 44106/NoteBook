import numpy as np

from hw4 import build_first_chapter_systems, build_quadratic_fit_problem, qr_least_squares, qr_solve


def test_qr_solve_matches_numpy_for_square_system():
    A = np.array(
        [
            [4.0, -2.0, 1.0],
            [1.0, 6.0, -2.0],
            [2.0, 1.0, 5.0],
        ]
    )
    b = np.array([7.0, 0.0, 9.0])

    expected = np.linalg.solve(A, b)
    actual = qr_solve(A, b)

    assert np.allclose(actual, expected, rtol=1e-12, atol=1e-12)


def test_qr_least_squares_matches_numpy_for_overdetermined_system():
    A = np.array(
        [
            [1.0, 0.0],
            [1.0, 1.0],
            [1.0, 2.0],
            [1.0, 3.0],
        ]
    )
    b = np.array([1.0, 2.0, 1.5, 3.5])

    expected, *_ = np.linalg.lstsq(A, b, rcond=None)
    actual = qr_least_squares(A, b)

    assert np.allclose(actual, expected, rtol=1e-12, atol=1e-12)


def test_quadratic_table_fit_is_exact():
    A, y = build_quadratic_fit_problem()

    coeffs = qr_least_squares(A, y)

    assert np.allclose(coeffs, np.array([1.0, 1.0, 1.0]), rtol=1e-12, atol=1e-12)
    assert np.linalg.norm(A @ coeffs - y, ord=2) < 1e-12


def test_qr_solve_returns_finite_small_residual_for_ill_conditioned_textbook_system():
    _, A, b, _ = build_first_chapter_systems()[0]

    x = qr_solve(A, b)

    assert np.all(np.isfinite(x))
    assert np.linalg.norm(A @ x - b, ord=np.inf) < 1e-10
