def add_binary_integers(A, B, n):
    C = [0] * (n + 1)
    carry = 0
    for i in range(n):
        sum_bit = A[i] + B[i] + carry
        C[i] = sum_bit % 2 # ビット和の結果の下位ビットを取得
        carry = sum_bit // 2 # sum_bitが2以上の場合は繰り上がりを計算
    C[n] = carry
    return C[::-1]

# 例1: A = 1101 (13), B = 1011 (11)
A = [1, 0, 1, 1]
B = [1, 1, 0, 1]
n = len(A)

# 二進数の和を計算
C = add_binary_integers(A, B, n)

# 結果の表示
print("C:", C)  # 出力: [0, 0, 0, 1, 1]  → 11000 (24)