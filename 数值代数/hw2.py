import numpy as np

# 1. 不选主元的 Gauss 消去法
def gauss_no_pivoting(A, b):
    n = len(b)
    U = A.astype(float).copy()
    y = b.astype(float).copy()
    for k in range(n - 1):
        if U[k, k] == 0: return np.full(n, np.nan)
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            y[i] -= m * y[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# 2. 列主元的 Gauss 消去法
def gauss_partial_pivoting(A, b):
    n = len(b)
    U = A.astype(float).copy()
    y = b.astype(float).copy()
    for k in range(n - 1):
        pivot = k + np.argmax(np.abs(U[k:, k]))
        if pivot != k:
            U[[k, pivot]] = U[[pivot, k]]
            y[[k, pivot]] = y[[pivot, k]]
        if U[k, k] == 0: return np.full(n, np.nan)
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            y[i] -= m * y[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# 3. Cholesky 分解 (平方根法)
def cholesky_solve(A, b):
    n = len(A)
    L = A.astype(float).copy()
    for k in range(n):
        if L[k, k] <= 0: 
            return np.full(n, np.nan)
        L[k, k] = np.sqrt(L[k, k])
        if k < n - 1:
            L[k+1:, k] = L[k+1:, k] / L[k, k]
            for j in range(k+1, n):
                L[j:, j] = L[j:, j] - L[j:, k] * L[j, k]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(L[i+1:, i], x[i+1:])) / L[i, i]
    return x

# 4. LDL^T 分解 (改进的平方根法)
def ldlt_solve(A, b):
    n = len(A)
    M = A.astype(float).copy()
    v = np.zeros(n)
    for j in range(n):
        for i in range(j):
            v[i] = M[j, i] * M[i, i]
        M[j, j] = M[j, j] - np.dot(M[j, :j], v[:j])
        if M[j, j] == 0: return np.full(n, np.nan)
        if j < n - 1:
            for k in range(j+1, n):
                M[k, j] = (M[k, j] - np.dot(M[k, :j], v[:j])) / M[j, j]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(M[i, :i], y[:i])
    z = np.zeros(n)
    for i in range(n):
        z[i] = y[i] / M[i, i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = z[i] - np.dot(M[i+1:, i], x[i+1:])
    return x

if __name__ == "__main__":
    # 题目 2.(1) 100 阶对称正定三对角方程组
    n1 = 100
    A1 = np.diag(np.full(n1, 10.0)) + np.diag(np.full(n1-1, 1.0), -1) + np.diag(np.full(n1-1, 1.0), 1)
    np.random.seed(42)
    b1 = np.random.rand(n1)
    x_exact1 = np.linalg.solve(A1, b1)

    # 题目 2.(2) 40 阶 Hilbert 矩阵方程组
    n2 = 40
    A2 = np.zeros((n2, n2))
    for i in range(n2):
        for j in range(n2):
            A2[i, j] = 1.0 / (i + j + 1)
    b2 = np.sum(A2, axis=1)
    x_exact2 = np.ones(n2)

    # 测试与误差计算
    def test_and_print(A, b, x_exact, title):
        print("="*50)
        print(title)
        print("="*50)
        methods = {
            "不选主元 Gauss": gauss_no_pivoting,
            "列主元 Gauss": gauss_partial_pivoting,
            "平方根法 (Cholesky)": cholesky_solve,
            "改进的平方根法 (LDL^T)": ldlt_solve
        }
        for name, func in methods.items():
            x_calc = func(A, b)
            if np.isnan(x_calc).any():
                print(f"{name:<20}: \t数值崩溃 (由于病态矩阵导致非正定或除零)")
            else:
                err = np.max(np.abs(x_calc - x_exact))
                print(f"{name:<20}: \t最大无穷范数误差 = {err:.4e}")
        print("\n")

    test_and_print(A1, b1, x_exact1, "测试题 1：100阶对称正定三对角矩阵")
    test_and_print(A2, b2, x_exact2, "测试题 2：40阶 Hilbert 矩阵")