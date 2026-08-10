import numpy as np
from scipy.linalg import hilbert

# 前置算法：列主元 Gauss 消去法
def gauss_partial_pivoting(A, b):
    n = len(b)
    U = A.astype(float).copy()
    y = b.astype(float).copy()
    
    for k in range(n - 1):
        pivot = k + np.argmax(np.abs(U[k:, k]))
        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            y[[k, pivot]] = y[[pivot, k]]
            
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            y[i] -= m * y[k]
            
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# 算法 2.5.1: 估计矩阵 1-范数 (优化法)
def estimate_inv_norm_inf(A):
    """
    为了估计 A 的无穷范数条件数，需要计算 ||A^{-1}||_inf。
    根据范数性质：||A^{-1}||_inf = ||(A^T)^{-1}||_1
    因此，我们将算法 2.5.1 应用于 B = (A^T)^{-1}
    """
    n = A.shape[0]
    x = np.ones(n) / n
    k = 1
    max_iter = 15
    iters = 0
    est_norm = 0
    
    while k == 1 and iters < max_iter:
        iters += 1
        
        w = np.linalg.solve(A.T, x)
        
        v = np.sign(w)
        v[v == 0] = 1.0  # 避免 sign(0)=0，确保属于 {-1, 1}
        
        z = np.linalg.solve(A, v)
        
        z_norm_inf = np.max(np.abs(z))
        z_dot_x = np.dot(z, x)
        
        if z_norm_inf <= z_dot_x + 1e-12:
            est_norm = np.linalg.norm(w, 1)
            k = 0
        else:
            j = np.argmax(np.abs(z))
            x = np.zeros(n)
            x[j] = 1.0
            est_norm = np.linalg.norm(w, 1)
            k = 1
            
    return est_norm

def estimate_cond_inf(A):
    """估计矩阵 A 的无穷范数条件数"""
    norm_A_inf = np.max(np.sum(np.abs(A), axis=1))
    norm_A_inv_inf = estimate_inv_norm_inf(A)
    return norm_A_inf * norm_A_inv_inf

# 任务 1：估计 Hilbert 矩阵的无穷范数条件数
print("="*60)
print("任务 (1): 5 到 20 阶 Hilbert 矩阵的无穷范数条件数估计")
print("="*60)
print(f"{'n':<5} | {'估计条件数':<20} | {'精确条件数(验证用)':<20}")
print("-" * 55)
for n in range(5, 21):
    H = hilbert(n)
    cond_est = estimate_cond_inf(H)
    cond_exact = np.linalg.cond(H, np.inf)
    print(f"{n:<5} | {cond_est:<20.4e} | {cond_exact:<20.4e}")

# 任务 2：特定矩阵 A_n 的计算解精度估计
print("\n" + "="*70)
print("任务 (2): 特定矩阵 A_n 的精度估计与真实相对误差比较")
print("="*70)
print(f"{'n':<5} | {'无穷范数条件数':<15} | {'后验精度估计界':<15} | {'真实相对误差':<15}")
print("-" * 70)

for n in range(5, 31):
    A = np.eye(n)
    for i in range(1, n):
        for j in range(i):
            A[i, j] = -1.0
    A[:, n-1] = 1.0
    
    np.random.seed(n)
    x_exact = np.random.rand(n)
    b = A @ x_exact
    
    x_hat = gauss_partial_pivoting(A, b)
    
    true_rel_error = np.max(np.abs(x_hat - x_exact)) / np.max(np.abs(x_exact))
    
    cond_est = estimate_cond_inf(A)
    r = b - A @ x_hat
    
    norm_A_inf = np.max(np.sum(np.abs(A), axis=1))
    norm_x_hat_inf = np.max(np.abs(x_hat))
    norm_r_inf = np.max(np.abs(r))
    
    est_precision = 0
    if norm_x_hat_inf > 0:
        est_precision = cond_est * (norm_r_inf / (norm_A_inf * norm_x_hat_inf))
        
    if n % 5 == 0 or n == 5 or n == 30:
        print(f"{n:<5} | {cond_est:<15.4e} | {est_precision:<15.4e} | {true_rel_error:<15.4e}")