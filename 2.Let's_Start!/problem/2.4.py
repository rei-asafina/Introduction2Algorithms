def merge_and_count(A, p, q, r):
    n_L = q - p + 1
    n_R = r - q
    L = A[p:q+1]
    R = A[q+1:r+1]
    i, j, k = 0, 0, p
    inv_count = 0
    
    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            inv_count += (n_L - i)
            j += 1
        k += 1
    
    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1
    
    return A, inv_count


def sort_and_count(A, p, r):
    if p >= r:
        return A, 0
    q = (p + r) // 2
    A, left_inv = sort_and_count(A, p, q)
    A, right_inv = sort_and_count(A, q + 1, r)
    A, split_inv = merge_and_count(A, p, q, r)
    total_inv = left_inv + right_inv + split_inv
    return A, total_inv

A = [2, 3, 8, 6, 1]
sorted_A, inv_count = sort_and_count(A, 0, len(A) - 1)

print(f"ソート済みの配列: {sorted_A}")
print(f"反転数: {inv_count}")
