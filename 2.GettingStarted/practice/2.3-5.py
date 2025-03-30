def insertion_sort_recursive(A, n):
    # ベースケース: 長さ1以下ならすでにソート済み
    if n <= 1:
        return
    
    # 再帰的に A[0:n-1] をソート
    insertion_sort_recursive(A, n - 1)
    
    # A[n-1] を適切な位置に挿入
    key = A[n - 1]
    i = n - 2
    
    # A[n-1] をソート済みの部分配列 A[0:n-1] に挿入
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    
    A[i + 1] = key

A = [5, 3, 8, 6, 2, 7]
n = len(A)
insertion_sort_recursive(A, n)
print("ソート結果:", A)
