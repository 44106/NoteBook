import numpy as np

def gauss_no_pivoting(A, b):
    n = len(b)
    U = A.astype(float).copy()
    y = b.astype(float).copy()
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            y[i] -= m * y[k]
            
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
        
    return x

def gauss_partial_pivoting(A, b):
    n = len(b)
    U = A.astype(float).copy()
    y = b.astype(float).copy()
    
    for k in range(n - 1):
        pivot_row = k + np.argmax(np.abs(U[k:, k]))
        if pivot_row != k:
            U[[k, pivot_row], :] = U[[pivot_row, k], :]
            y[[k, pivot_row]] = y[[pivot_row, k]]
            
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            y[i] -= m * y[k]
            
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
        
    return x

if __name__ == "__main__":
    n = 84
    A = np.diag(np.full(n, 6.0)) + np.diag(np.full(n-1, 8.0), -1) + np.diag(np.full(n-1, 1.0), 1)
    
    b = np.full(n, 15.0)
    b[0] = 7.0
    b[-1] = 14.0

    x_exact = np.ones(n)

    x_no_pivot = gauss_no_pivoting(A, b)
    x_partial_pivot = gauss_partial_pivoting(A, b)

    error_no_pivot = np.max(np.abs(x_no_pivot - x_exact))
    error_partial_pivot = np.max(np.abs(x_partial_pivot - x_exact))

    print("84阶线性方程组求解结果对比")
    print(f"精确解 (前10项): {x_exact[:10]}")
    print(f"精确解 (后10项): {x_exact[-10:]}\n")
    
    print(f"不选主元法计算结果 (后10项): {np.round(x_no_pivot[-10:], 6)}")
    print(f"不选主元法最大误差: {error_no_pivot:.6e}\n")
    
    print(f"列主元法计算结果 (后10项): {np.round(x_partial_pivot[-10:], 6)}")
    print(f"列主元法最大误差: {error_partial_pivot:.6e}\n")
