def two_sum(S, x):
    S.sort()  # ソート O(n log n)
    i = 0
    j = len(S) - 1

    while i < j:
        total = S[i] + S[j]
        if total == x:
            return True
        elif total < x:
            i += 1
        else:
            j -= 1
    return False

S = [3, 1, 7, 5, 9]
x = 10
print(two_sum(S, x))
