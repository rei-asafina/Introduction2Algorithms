def insertion_sort_desc(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

# 配列の例
A = [31, 41, 59, 26, 41, 58]
print("元の配列:", A)

# 降順でソート
insertion_sort_desc(A)
print("降順ソート後の配列:", A)
