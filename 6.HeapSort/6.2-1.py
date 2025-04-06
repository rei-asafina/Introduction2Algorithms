def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

A = [16, 4, 10, 20, 7, 9, 3, 2, 8, 1]

heap_size = len(A)
i = 1
max_heapify(A, i, heap_size)
print("After max_heapify:", A)

