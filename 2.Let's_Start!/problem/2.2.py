def bubble_sort(A, n):
    for i in range(1, n):  # i は 1 から n-1 まで
        print(i)
        for j in range(n - 1, i - 1, -1):  # j は n-1 から i まで逆順
            print(" ",A[j],A[j-1])
            if A[j] < A[j - 1]:  # 左の要素が大きければ交換
                A[j], A[j - 1] = A[j - 1], A[j]  # 要素を交換

A = [5, 3, 8, 4, 2]
n = len(A)
bubble_sort(A, n)
print("ソート後の配列:", A)
