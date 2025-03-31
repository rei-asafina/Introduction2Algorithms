import numpy as np

def matrix_add_recursive(A, B):
    # 行列のサイズを取得
    n = A.shape[0]
    
    # ベースケース：1x1行列の場合
    if n == 1:
        C = np.array([[A[0, 0] + B[0, 0]]])
        return C
    
    # 中間サイズ（n//2）
    m = n // 2

    # 部分行列の分割（インデックス計算によるアクセス）
    A11, A12, A21, A22 = A[:m, :m], A[:m, m:], A[m:, :m], A[m:, m:]
    B11, B12, B21, B22 = B[:m, :m], B[:m, m:], B[m:, :m], B[m:, m:]

    # 再帰的に部分行列の和を計算
    C11 = matrix_add_recursive(A11, B11)
    C12 = matrix_add_recursive(A12, B12)
    C21 = matrix_add_recursive(A21, B21)
    C22 = matrix_add_recursive(A22, B22)

    # 結果の結合
    C_top = np.hstack((C11, C12))  # 上側の行の結合
    C_bottom = np.hstack((C21, C22))  # 下側の行の結合
    C = np.vstack((C_top, C_bottom))  # 行列全体の結合
    
    return C

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

B = np.array([
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
])

C = matrix_add_recursive(A, B)
print("行列 A と B の和は:")
print(C)
