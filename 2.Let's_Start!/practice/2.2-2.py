def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

A = [64, 25, 12, 22, 11]
print("ソート前の配列:", A)
selection_sort(A)
print("ソート後の配列:", A)
