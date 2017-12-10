"""
@jetou
@date : 2017/12/9
@algorithms: randomized_select
"""

import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_select(A, p, r, i):
    # if p == r:
    #     return A[p]

    q = randomized_partition(A, p, r)
    print q,A
    if q == i:
        return A[q]
    elif q > i :
        return randomized_select(A, p, q-1, i)
    return randomized_select(A, q+1, r, i)

A = [2,34,5,1,6,7,9]
print randomized_select(A, 0, 6, 0)
