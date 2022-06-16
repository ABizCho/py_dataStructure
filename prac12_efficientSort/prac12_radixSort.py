import collections


def radix_sort(A) :
    queues = []
    for i in range(BUCKETS) :
        queues.append(collections.deque())
        
    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) :
            queues[(A[i]//factor) % 10].append(A[i])

        i=0
        for b in range(BUCKETS) :
            while queues[b] :
                A[i] = queues[b].popleft()
                i += 1
        factor *= 10
        print('Step', d+1, A)
        
import random
BUCKETS = 10
DIGITS = 4
data = []
for i in range(10) :
    data.append(random.randint(1,9999))
radix_sort(data)
print('Radix:', data)