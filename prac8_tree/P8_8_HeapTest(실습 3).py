#P8_8 ----------------
def isMinHeapIter(A) :
    n = len(A)-1
    for i in range(1, n) :
        l = i * 2
        r = i * 2 + 1
        if l <= n and A[l] < A[i] : return False
        if r <= n and A[r] < A[i] : return False
    return True


def isMaxHeapIter(A) :
    n = len(A)-1
    for i in range(1, n) :
        l = i * 2
        r = i * 2 + 1
        if l <= n and A[l] > A[i] : return False
        if r <= n and A[r] > A[i] : return False
    return True

Heap = [-1, 1, 4, 2, 7, 5, 3, 3, 7, 8, 9]

print(Heap)
print("isMinHeapIter:", isMinHeapIter(Heap))
print(Heap)

print("isMaxHeapIter:", isMaxHeapIter(Heap))
print(Heap)

