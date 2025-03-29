def binary_search(A, v, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if A[mid] == v:
        return mid
    elif A[mid] > v:
        return binary_search(A, v, low, mid - 1)
    else:
        return binary_search(A, v, mid + 1, high)


# ✅ 動作確認
A = [1, 3, 5, 7, 9, 11, 13, 15]
v = 13
result = binary_search(A, v, 0, len(A) - 1)

if result != -1:
    print(f"{v} はインデックス {result} で見つかりました。")
else:
    print(f"{v} は見つかりませんでした。")
